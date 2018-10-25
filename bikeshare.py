import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nWhich city data would you like to see. chicago, new york or washington')
    city=input().lower()
    while city not in ( 'chicago' , 'new york' , 'washington'):
        print('\nCity name you have entered is {} , which is not a valid city. Please enter valid input (chicago, new york or washington)'.format(city))
        city=input().lower()
        if city in ( 'chicago' , 'new york' , 'washington'):
            break
        else :
            continue
    print('\nSure. We will now have a look on {} data'.format(city))
    print('\nWould you like to filter data on month, day or both ( Type none for no filter required )')
    filter_value=input().lower()
    while filter_value not in ( 'month' , 'day' , 'both','none'):
        print('\nFilter value you entered is {} , while is not a valid input. Please enter a valid input (eg :month,day,both,none)'.format(filter_value))
        filter_value=input().lower()
        if filter_value in ( 'month' , 'day' , 'both','none'):
            break
        else :
            continue
    if filter_value=='month':
     # TO DO: get user input for month (all, january, february, ... , june)
        print('\nEnter the month that needs to be filtered on.\nBelow are the valid inputs\n   january\n   febraury\n   march\n   april\n   may\n   june\n   all')
        month=input().lower()
        day='all'
        while month not in ('january','febraury','march','april','may','all'):
            print('\nMonth value entered {} is not a valid.\nPlease enter a valid input.Below are the valid inputs:\n   january\n   febraury\n   march\n   april\n   may\n   june\n   all'.format(month))
            month=input().lower()
            
            if month  in ('january','febraury','march','april','may','all'):
                break
            else:
                continue
    elif filter_value=='day':
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

        print('\nEnter the day that needs to be filtered on.\nBelow are the valid inputs\n   monday\n   tuesday\n   wednesdey\n   thursday\n   friday\n   saturday\n   sunday\n   all')
        day=input().lower()
        month='all'
        while day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('\nDay filter value entered {} is not valid. Please enter a valid month .\nBelow are the valid inputs\n   monday\n   tuesday\n   wednesdey\n   thursday\n   friday\n   saturday\n   sunday\n   all')
            day=input().lower()
            if day  in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
                break
            else:
                continue

        print('\nNow we will look at data for {}'.format(day))
    elif filter_value=='both':
        # TO DO: get user input for month (all, january, february, ... , june)
        print('\nEnter the month that needs to be filtered on.\nBelow are the valid inputs\n   january\n   febraury\n   march\n   april\n   may\n   june\n   all')
        month=input().lower()
        while month not in ('january','febraury','march','april','may','june','all'):
            print('\nEnter a valid month .\nBelow are the valid inputs\n   january\n   febraury\n   march\n   april\n   may\n   june\n   all')
            month=input().lower()
            if month  in ('january','febraury','march','april','may','june','all'):
                break
            else:
                continue
        
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

        print('\nEnter the day that needs to be filtered on.\nBelow are the valid inputs\n   monday\n   tuesday\n   wednesdey\n   thursday\n   friday\n   saturday\n   sunday\n   all')
        day=input().lower()

        while day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('\nEnter a valid month .\nBelow are the valid inputs\n   monday\n   tuesday\n   wednesdey\n   thursday\n   friday\n   saturday\n   sunday\n   all')
            day=input().lower()
            if day  in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
                break
            else:
                continue
        print('\nNow we will look at data for {} month and {} day'.format(month,day))
       
    elif filter_value=='none':
        month='all'
        day='all'
        print('\nNow we will look at data for {} month and {} day'.format(month,day))

    print('-'*40)
    return city, month, day

def load_data(city, month='all', day='all'):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    # find the most popular hour
    popular_month = df['month'].mode()[0]
    print('\nThe Most popular month:{}'.format(popular_month))

    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.week
    # find the most popular hour
    popular_week = df['week'].mode()[0]
    print('\nThe Most popular week:{}'.format(popular_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe Most popular hour:{}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('\nThe Most commonly used start station:{}'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nThe Most commonly used end station:{}'.format(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station']=df['Start Station'] + df['End Station']
    combined_station =df['Combined Station'].mode()[0]
    print('\nThe Most commonly used combined station:{}'.format(combined_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    #total_time=df.groupby(['Trip Duration']).sum()
    total_time=df['Trip Duration'].sum()
    print('\nTotal travel time {}'.format(total_time))

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('\nMean travel time {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].count()
    print('\nCounts of user types is {}'.format(user_type))

    # TO DO: Display counts of gender
    if city not in ('washington'):
        gender=df['Gender'].count()
        print('\nCounts of gender is {}'.format(gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Birth Year is {}'.format(earliest_year))    
        recent_year = df['Birth Year'].max()
        print('\nRecent Birth Year is {}'.format(recent_year))
        common_year = df['Birth Year'].mode()[0]
        print('\nCommon Birth Year is {}'.format(common_year))
    else:
        print('\nNo Gender and Birth Year value specified in file')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    print('\nWould you like to see first five rows of raw data...')
    row_count=5
    rdata=input()
    while rdata == 'yes':
        print(df.head(row_count))
        print('\nWould you like to see few more data')
        rdata=input()
        if rdata=='no':
            break
        else:
            row_count+=5
            continue
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()