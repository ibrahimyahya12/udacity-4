# test
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
Day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
username = input('enter your name ')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! mr/ms {} Let\'s explore some US bikeshare data!'.format(username))
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input('which city you want to check:'
                          '\n\n- chicago \n- new york city \n- washington there no jender \n\n> ')
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print('sorry there some error .'
                  '\n make sure your choice from the option \n> ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH:
        month_name = input('which month you want to check?'
                           '\n\n january \n- february \n- march'
                           '\n- april \n- may \n- june \n- all'
                           ' (if you want to select all months)\n\n> ')

        if month_name.lower() in MONTH:
            month = month_name.lower()
        else:
            print('sorry there some error.'
                  '\nmake sure your choice from the option')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in Day:
        day_name = input('\n what weekday you want to select ?'
                         '\n\n- monday \n- tuesday \n- wednesday'
                         '\n- thursday \n- friday \n- saturday \n- sunday'
                         '\n- all (if you want to select all days)\n\n> ')
        if day_name.lower() in Day:
            day = day_name.lower()
        else:
            print('sorry there some error.'
                  '\nmake sure your choice from the option\n> ')

    print('-' * 40)
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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH.index(month)
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df['month'].mode()[0]
    print("- this is the most common month = " + MONTH[com_month])

    # TO DO: display the most common day of week
    com_day_of_week = df['day_of_week'].mode()[0]
    print("- this is the most common day = " + com_day_of_week)

    # TO DO: display the most common start hour
    com_start_hour = df['hour'].mode()[0]
    print("- this is the most common start hour = " + str(com_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print("- this is the most common used start station : " +
          com_start_station)

    # TO DO: display most commonly used end station
    com_endstation = df['End Station'].mode()[0]
    print("- this is the most common used end station: "
          + com_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("- this is the most frequent combination from start station and end station trip  : " +
          str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\n\n this is the total travel time = \n" + str(total_travel_time))

    # TO DO: display mean travel time
    mean_of_travel_time = df['Trip Duration'].mean()
    print("- The mean of travel time = \n" + str(mean_of_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types = \n" + str(user_types))

    # TO DO: Display counts of gender 
    gander = df['Gender'].value_counts()
    print('the number of gender is {}'.format(gander))
    # TO DO: Display earliest, most recent, and most common year of birth
    first_birth = df['Birth Year'].min()
    print('\n\n- The first birth year of birth = \n {}'.format(first_birth))

    most_recent = df['Birth Year'].max()
    print('- The most recent year of birth = {}'.format(most_recent))

    most_common_birth = df['Birth Year'].mode()[0]
    print('- The most common year of birth = \n {}'
          .format(most_common_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    print(df.head())
    next = 0
    while True:
        view_raw_data = input(
            '\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n >')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_raw_data = input(
                '\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
