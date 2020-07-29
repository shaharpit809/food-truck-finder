from utils import query_utils

class FoodTruck():
    def __init__(self, applicant, location):
        self.applicant = applicant
        self.location = location
        
    def view_foodtrucks(data):
        all_food_trucks = []
            
        for foodtruck in data:
            ft_obj = FoodTruck(**foodtruck)
            all_food_trucks.append(ft_obj)
        
        print('applicant'.ljust(80), 'location')
        print('----------------------------------------------------------------------------------------------------------')
        for foodtruck in all_food_trucks:
            print(foodtruck.applicant.ljust(80), foodtruck.location)
        
        print('----------------------------------------------------------------------------------------------------------')

def main():        
    q = query_utils()
    page_num = 0
    offset = 0
    response = q.get_response(offset)
    
    #Check the status code of the response and display the necessary message.
    while response:
        if response.status_code == 200:
            data = response.json()
            
            if not data:
                print('Sorry, we are out of available food trucks options!')
                break
            
            FoodTruck.view_foodtrucks(data)
            
            print('Options : \'p\' for previous options, \'n\' for more amazing options, \'q\' for quitting')
            user_input = input('Wish to check out other amazing places to hog? Select : (p, n, q) - ')
            
            #Keep on asking the user for a valid input
            while user_input not in set(['p', 'n', 'q']):
                user_input = input('Please select a valid option from : (p, n, q) - ')
            
            if user_input == 'p':
                response, page_num = q.view_page(page_num, -1)
            elif user_input == 'n':
                response, page_num = q.view_page(page_num, 1)
            elif user_input == 'q':
                break
            
        elif response.status_code == 400:
            print('Bad request received. Please check the error message and make the necessary changes.')
            break
        elif response.status_code == 401:
            print('Something went wrong with the authentication. Please authenicate yourself and try again.')
            break
        elif response.status_code == 403:
            print('Unauthorized access. Please check all the permissions and authenicate yourself to try again.')
            break
        elif response.status_code == 404:
            print('Page not found. Please check your query and try again.')
            break
        elif response.status_code == 429:
            print('Too many request received. Rate limitation applied. Please use app token to reduce throttling.')
            break
        elif response.status_code == 500:
            print('Socrata server down. Please try again later.')
            break
            
    print('Hope you found the food truck of your choice!')

if __name__ == '__main__':
    main()