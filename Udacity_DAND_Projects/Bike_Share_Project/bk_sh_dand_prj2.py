# Setting my imports for the Bike Share Project

import time
import pandas as pd
import numpy as np

# Setting my DataFrames using my csv files: First I'll create a variable for the file path of each csv file
# then pass it to the .read_csv method in Pandas

# Creating a dictionary CITY_DATA to store my 3 city dataframes

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'
              }

months = {0: 'All', 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}

days = {0: 'All', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
        6: 'Saturday', 7: 'Sunday'}

def get_city():
    """
    Asks user to specify the city they would like to analyze.

    Returns:
        (str) city - name of the city to filter by
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Please select a city you would like to explore. Here are your choices: Chicago, "
                 "New York City, or Washington \n"
                 "Enter the name of the city you have selected as you see it displayed, here.")

    # This code will handle any incorrect inputs

    while city.lower() not in CITY_DATA:
        print("I'm sorry, your selection {} is not a valid city choice. Please choose a city from the"
              " provided list. \n".format(city))
        city = input("Please enter a valid city selection: \n ")

    # This code will handle correct inputs

    if city.lower() in CITY_DATA:
        print("Excellent, let's take a look at {}. \n".format(city.title()))

    return city

def get_day():
    """
    Asks user to specify the month they would like to analyze.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            prompt_day = ("Please enter the number of the corresponding day you'd like to filter " \
                          "your chosen dataset by. \n \n " \
                          "0: All \n 1: Monday \n 2: Tuesday \n 3: Wednesday \n 4: Thursday \n 5: Friday \n " \
                          "6: Saturday \n 7: Sunday \n\n " \
                          "Choose your filter here: ")

            day_fltr = int(input(prompt_day))

            day = days[day_fltr]

            break

        except ValueError:
            print("Please enter a valid filter number from the list: \n")

            continue

        except KeyError:
            print("Please enter a valid filter number from the list: \n")

            continue

    if day_fltr in days:
        print("Great! You've selected {} as you filter. \n\n".format(day))

    return day

def get_month():
    """
    Asks user to specify the month they would like to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """

    # get user input for month (all, january, february, ... , june) HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            prompt_mth = ("Please enter the number of the corresponding month you'd like to filter " \
                          "your chosen dataset by. \n \n " \
                          "0: All \n 1: January \n 2: February \n 3: March \n 4: April \n 5: May \n 6: June \n\n " \
                          "Choose your filter here: ")

            mth_fltr = int(input(prompt_mth))

            month = months[mth_fltr]

            break

        except ValueError:
            print("Please enter a valid filter number from the list: \n")

            continue

        except KeyError:
            print("Please enter a valid filter number from the list: \n")

            continue

    if mth_fltr in months:
        print("Great! You've selected {} as you filter. \n\n".format(month))

    return month

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')

    city = get_city()

    # Accessing data based on user input to define key parameters, Month, day, both or none at all.

    message = "Would you like to filter the {} dataset by Month, Day, Both or not at all? " \
              "For no filter, type 'All'. \n".format(city.title())

    filter_choice = input(message)

    choices = ['Month', 'Day', 'Both', 'All']

    # Setting up an if/elif chain to handle user input for filter choice

    if filter_choice == 'All' or filter_choice == 'all':

        day = days[0]

        month = months[0]

    elif filter_choice == 'Both' or filter_choice == 'both':

        return city, get_month(), get_day()

    elif filter_choice == 'Month' or filter_choice == 'month':

        day = days[0]

        return city, get_month(), day

    elif filter_choice == 'Day' or filter_choice == 'day':

        month = months[0]

        return city, month, get_day()

    else:

        print("Im sorry, you've entered an invalid filter. \n")
        filter_choice = int(input("Please enter a valid filter from the list: \n"))


    print('-'*40)
    return city, month, day

def load_data(city, month = 'All', day = 'All'):
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
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times For Travel Statistics...\n')
    start_time = time.time()

    # display the most common month

    most_com_mth = months[df['month'].mode()[0]]

    print("The most common month for travel within this dataset is {}. \n".format(most_com_mth))

    # display the most common day of week

    most_com_dow = df['day_of_week'].mode()[0]

    print("The most common day of the week for travel is {}. \n".format(most_com_dow))

    # display the most common start hour

    popular_hour = df['hour'].mode()[0]

    print("The most frequent start hour is {} o'clock. \n".format(popular_hour - 12))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_com_strt_st = df['Start Station'].mode()[0]

    print("The most commonly used start station for travel is {}. \n".format(most_com_strt_st))

    # display most commonly used end station

    most_com_end_st = df['End Station'].mode()[0]

    print("The most commonly used end station for travel is {}. \n".format(most_com_end_st))

    # display most frequent combination of start station and end station trip

    most_frq_st_combo = df.groupby(['Start Station', 'End Station']).size().nlargest()

    print("The most common combination of Start/End station trips and there counts in this dataset is: \n \n {}"
          .format(most_frq_st_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration Statistics...\n')
    start_time = time.time()

    # display total travel time (divided by 60 to express total travel time in minutes not seconds)

    tot_trvl_time = (df['Trip Duration'].sum()) / 60

    print("The total travel time for the filter(s) you've selected is {:.2f} minutes. \n".format(tot_trvl_time))

    # display mean travel time (divided by 60 to express total travel time in minutes not seconds)

    avg_trvl_time = (df['Trip Duration'].mean()) / 60

    print("The average travel time for the filter(s) you've selected is {:.2f} minutes.".format(avg_trvl_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()

    print("There are two kinds of patrons within your chosen dataset: Subscriber and Customer. \n"
          "The following statistic shows, in comparison, their total sum "
          "within any other parameters you may have set, like month, or day. \n \n{}".format(user_types))

    # Display counts of gender

    try:
        gender_types = df['Gender'].value_counts()

        print("\nThe following statistic compares gender within your dataset: \n \n{}".format(gender_types))

    except:
        print("We're sorry, but gender specific data is not present in Washington's dataset. \n")


    # Display earliest, most recent, and most common year of birth

    try:
        early_yob = df['Birth Year'].max()
        mst_rec_yob = df['Birth Year'].min()
        mst_com_yob = df['Birth Year'].mode()[0]

        print("\nWith this statistic, let's compare the birth year between bikeshare patrons. \n"
              "We'll calculate the eldest customer, the yougest, and most common birth year. \n \n{}\n{}\n{}"
              .format(early_yob, mst_rec_yob, mst_com_yob))
    except:
        print("We're sorry, but Birth Year data for each patron is not tracked in Washington's dataset. \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data():
    """
    Asks user to specify the city they would like to analyze and return a data frame of unfiltered data.

    Returns:
        (str) city - name of the city to filter by
    """
    # Getting user input to review raw/unfiltered data
    raw_data_prompt = ("\nWould you like to continue your exploration of US bikeshare data and analyze "
                       "some raw/unfiltered data for one of the cities available? \nEnter yes or no.")

    raw_data_input = input(raw_data_prompt)

    if raw_data_input.lower() == 'yes':
        city = get_city()
        df = load_data(city)
        print(df.head())

        x = 0
        y = 5

        while x < len(df.index):
            more_rows_prompt = ("Would you like to analyze the next 5 rows of unfiltered data? Enter 'Yes' or 'No': ")
            more_rows_input = input(more_rows_prompt)
            if more_rows_input.lower() == "yes":
                x = x + 5
                y = y + 5
                print(df.iloc[x:y])
            else:
                break
    else:
        if raw_data_input.lower() == 'no':
            exit()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() == 'yes':
            return get_raw_data()
        else:
            if restart.lower() != 'yes':
                break

if __name__ == "__main__":
    main()
