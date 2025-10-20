import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print("Hi! Let's explore some US bikeshare data!")
    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        city = input("Choose a city (chicago, new york city, washington): ").strip().lower()
        if city in cities:
            break
        print("Invalid city. Please try again later.")

    while True:
        month = input("Choose a month (all, january, february, march, april, may, june): ").strip().lower()
        if month in months:
            break
        print("Invalid month. Please try again.")

    while True:
        day = input("Choose a day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").strip().lower()
        if day in days:
            break
        print("Invalid day. Please try again.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    if not df.empty:
        print(f"Most common month: {df['month'].mode()[0].title()}")
        print(f"Most common day of week: {df['day_of_week'].mode()[0].title()}")
        print(f"Most common start hour: {int(df['hour'].mode()[0])}:00")
    else:
        print("No data available for the selected filters.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    if not df.empty:
        print(f"Most commonly used start station: {df['Start Station'].mode()[0]}")
        print(f"Most commonly used end station: {df['End Station'].mode()[0]}")
        combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print(f"Most frequent trip: {combo[0]} -> {combo[1]}")
    else:
        print("No data available for the selected filters.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    if not df.empty:
        total_seconds = int(df['Trip Duration'].sum())
        mean_seconds = float(df['Trip Duration'].mean())
        def fmt(sec):
            sec = int(sec)
            h = sec // 3600
            m = (sec % 3600) // 60
            s = sec % 60
            return f"{h}h {m}m {s}s"
        print(f"Total travel time: {fmt(total_seconds)}")
        print(f"Mean travel time: {fmt(mean_seconds)}")
    else:
        print("No data available for the selected filters.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    if not df.empty:
        if 'User Type' in df.columns:
            print("User Types:")
            print(df['User Type'].value_counts().to_string())
        if 'Gender' in df.columns:
            print("\nGender:")
            print(df['Gender'].value_counts().to_string())
        if 'Birth Year' in df.columns:
            print("\nBirth Year:")
            print(f"Earliest: {int(df['Birth Year'].min())}")
            print(f"Most recent: {int(df['Birth Year'].max())}")
            print(f"Most common: {int(df['Birth Year'].mode()[0])}")
        if 'Gender' not in df.columns and 'Birth Year' not in df.columns:
            print("Gender and Birth Year data not available for this city.")
    else:
        print("No data available for the selected filters.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    i = 0
    while True:
        show_data = input("\nWould you like to see the raw data? Yes or No: ").strip().lower()
        if show_data != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5
        while True:
            next_data = input("\nWould you like to see next raw data? Yes or No: ").strip().lower()
            if next_data == 'yes':
                print(df.iloc[i:i+5])
                i += 5
            elif next_data == 'no':
                return
            else:
                print("Please type Yes or No.")

def main():
    while True:
        city, month, day = get_filters()
        try:
            df = load_data(city, month, day)
        except FileNotFoundError:
            print(f"File not found for {city}: {CITY_DATA[city]}")
            restart = input("Would you like to restart? Enter yes or no: ").strip().lower()
            if restart != 'yes':
                break
            else:
                continue

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no: ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
