import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
              """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    
 # TO DO: get user input for city (chicago, new york city, washington=
    city = input('would you like to see data for Chicago, New York City, Washington or all ?\n').lower()  
    
    # lower() is used to get input in any format
    
    
    while(True):
        if(city == 'chicago' or city == 'new york city' or city == 'washington' or city == 'all'):
            break
        else:
            city = input('Enter Correct city: ').lower()
           
     # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
     #lower is used to get input in any format

    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june'                  or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower()
             #print("Enter vaild month name")
         
  
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Which day of the week?Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday or all to display data of all                        days\n").lower()
            
    while(True):
      
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thrusday' or day == 'friday' or day == 'saturday'               or day == 'sunday' or day == 'all'):
            break
        else:
           day=input('Enter Valid day:').lower()
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
                             

#convert Start Time column to datetime                          
    df['Start Time'] = pd.to_datetime(df['Start Time'])

  #extract month and day of week from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
              
 #filter by month if applicable
    if month != 'all':
        
          #use the index of the months list to get the corresponding integer
         months = ['january','february','march','april','may','june']
         month = months.index(month) + 1
                          
 #Filter by day of week to create the new dataframe
         df=df[df['month'] == month]  
                          
# filter by data by week
    if day != 'all':
        
   #Filters by day of week to create the new dataframe
         df=df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

 # TO DO: display the most common month
    
    #Use mode method to find the most popular month
    common_month=df['month'].mode()[0]
    print('The most common month is :', common_month)


 # TO DO: display the most common day of week
    
    #Uses mode method to find the most popular month
    common_day_week=df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day_week)

 # TO DO: display the most common start hour
    
    #Extract hour from the Start Time column to create an hour column
    df['hour']=df['Start Time'].dt.hour
    
    common_start_hour=df['hour'].mode()[0]
    print('The most common hour:', str(common_start_hour))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

 # TO DO: display most commonly used start station
    Start_Station=df['Start Station'].mode()[0]
    print('The most common used start station is :', Start_Station)

    # TO DO: display most commonly used endstation
    End_Station=df['End Station'].mode()[0]
    print('The most common used end station :', End_Station)

 # TO DO: display most frequent combination of start station and end station trip
    Combination_Station=df.groupby(['Start Station', 'End Station']).count() 
    print('Most commonly used combo of Start Station and End Station:', Start_Station,End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 # TO DO: display total travel time
    totaltravel_time = df['Trip Duration'].sum()
    print("The total travel time from the given data :",totaltravel_time)

 # TO DO: display mean travel time
    meantravel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given data:", meantravel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

 # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of User Types from the given data :\n', str(user_types))
    
 # TO DO: Display counts of gender
    if('Gender' in df):
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given data :\n", str(gender))
     
  

 # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
       earliest_year=df['Birth Year'].min()
       print("\n Earliest Year is {} \n". format(int(earliest_year)))
        
       recent_year=df['Birth Year'].max()
       print("\n Most Recent Year is {} \n". format(int(recent_year)))
        
       most_common_birthyear=df['Birth Year'].mode()[0]
       print("\n Most Popular Birth Year is {} \n". format(int(most_common_birthyear)))
                    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data != 'yes':
            break
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
	     main()
