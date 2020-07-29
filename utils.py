import datetime
import requests
import os

class query_utils():
    def __init__(self):
        """
        Initializing few basic variables.
        """
        self.display_fields = ['applicant', 'location']
        self.datetime_now = datetime.datetime.now()
        self.display_limit = 10
        
    def get_weekday(self):
        """
        Weekday number for Socrata's data ranges from 1 - 7 for Mon - Sun.
        Weekday number for the below code ranges from 0 - 6 for Mon - Sun. 
        Get the appropriate weekday number. 
        """
        weekday = self.datetime_now.weekday() + 1
        if weekday == 7:
            return 0
        else:
            return weekday
    
    def get_currentTime(self):
        """
        Get the current time in 24 hours format.
        """
        hour = self.datetime_now.hour
        minute = self.datetime_now.minute
        
        return '\'' + str(hour) + ':' + str(minute) + '\''
    
    def generate_query(self, offset):
        """
        Generate SoQL query to fetch the required data.
        Read more about SoQL from - https://dev.socrata.com/docs/queries/
        """        
        all_display_fields = ', '.join(self.display_fields)
        query = ("?$select={0}"
                 "&$where=dayorder={1} and {2} between start24 and end24"
                 "&$order=applicant ASC"
                 "&$limit={3}"
                 "&$offset={4}"
                 ).format(all_display_fields,
                         self.get_weekday(),
                         self.get_currentTime(),
                         self.display_limit,
                         offset)
        
        return query
    
    def get_response(self, offset):
        """
        Get a response object by making a http call to Socrata's API.
        """
        base_url = "http://data.sfgov.org/resource/bbb8-hzi6.json"
        query = self.generate_query(offset)
        main_query = base_url + query
        
        try:
            if os.environ.get('APP_TOKEN') is not None:
                header = {'X-App-Token': os.environ.get('APP_TOKEN')}
                response = requests.get(main_query, headers = header)
            else:
                response = requests.get(main_query)
        #If no response object is returned, exit and check the url
        except requests.exceptions.RequestException as e:
            print('Failed to establish a connection. Please check the url.')
            return
        
        return response

    def view_page(self, curr_page, page_num):
        """
        View the next or the previous page. 
        If there are no enteries for previous page, display the first 10 food trucks.
        """
        curr_page += page_num
        offset = self.display_limit * curr_page
        if curr_page < 0 or offset < 0:
            curr_page, offset = 0, 0
            
        response = self.get_response(offset)
        
        return response, curr_page