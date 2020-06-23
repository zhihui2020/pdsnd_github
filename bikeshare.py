#This file is used for Udacity program
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ("Would you like to see data for chicago, new york city or washington? ")

    #We need a minor change here.
    #Think of a scenario where the user enters case sensitive data such as "Chicago" , "chiCAgo" etc .....
    #Think of a way to implement case agnost inputs. We need this as per the rubric.
    city = city.lower()
    #
    filt = input ("Would you like to filter the data by month, day or both? ")

    # TO DO: get user input for month (all, january, february, ... , june)
    if filt == 'month':
       month = input ("Which month? january, february, march, april, may, june or all? ")
       month = month.lower()
       print('-'*40)
       return city, month, 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif filt == 'day':
         day = input ("Which day? monday, tuesday, wednesday, thursday,friday, saturday, sunday or all? ")
         day = day.lower()
         print('-'*40)
         return city, 'all', day
    else:
        month = input ("Which month? january, february, march, april, may, june or all? ")
        day = input ("Which day? monday, tuesday, wednesday, thursday,friday, saturday, sunday or all? ")
        month = month.lower()
        day = day.lower()
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)

    # TO DO: display the most common start hour

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' AND ' + df['End Station']
    popular_combined_station = df['Station Combination'].mode()[0]
    print('Most Popular Combined Station:', popular_combined_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total Duration:', total_duration)

    # TO DO: display mean travel time
    avg_duration = total_duration / df['Trip Duration'].count()
    print('Average Duration:', avg_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def gender_birth_stats(df):
    """Displays statistics on bikeshare users' gender and birth year."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of gender

    gender_types = df['Gender'].value_counts()
    print(gender_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth

    earliest_birth_year = int(df['Birth Year'].min())
    most_recent_birth_year = int(df['Birth Year'].max())
    most_common_birth_year = int(df['Birth Year'].mode()[0])
    print("\nEarliest birth year is %s" % earliest_birth_year)
    print("\nMost recent birth year is %s" % most_recent_birth_year)
    print("\nMost common birth year is %s" % most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # a tempory dataset to show raw data
        df1 = load_data(city, month, day)
        for i in range(len(df)):
            raw_data = input('\nWould you like to see 5 lines of the raw data? Enter yes or no.\n')
            i=5*(i+1)
            if raw_data.lower() == 'yes':
                print(df1.head())
                df1 = df1.drop([i-5,i-4,i-3,i-2,i-1], axis = 0)
            else:
                break

        if city != 'washington':
           time_stats(df)
           station_stats(df)
           trip_duration_stats(df)
           user_stats(df)
           gender_birth_stats(df)

        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
