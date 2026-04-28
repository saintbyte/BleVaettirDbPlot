#!/usr/bin/env python3
import argparse
import sqlite3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def main():
    parser = argparse.ArgumentParser(description='Generate chart from SQLite readings')
    parser.add_argument('--db', default='readings.db', help='SQLite database path')
    parser.add_argument('--sensor-name', required=True, help='Sensor name to filter')
    parser.add_argument('--type', required=True, help='Type to filter')
    parser.add_argument('--output', default='chart.png', help='Output image path')
    parser.add_argument('--width', type=int, default=2000, help='Image width in pixels')
    parser.add_argument('--height', type=int, default=600, help='Image height in pixels')
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)
    query = '''
        SELECT timestamp,
               value,
               unit
        FROM readings
        WHERE sensor_name = ? AND type = ?
        ORDER BY timestamp
    '''
    df = pd.read_sql_query(query, conn, params=(args.sensor_name, args.type))
    conn.close()

    if df.empty:
        print('No data found')
        return

    #df['timestamp'] = pd.to_datetime(df['timestamp'])
    orig_len = len(df)

    num_points = orig_len
    if num_points > args.width:
        step = num_points // args.width
        df = df.iloc[::step].reset_index(drop=True)
        print(f'Aggregated: {orig_len} -> {len(df)} points')

    min_val = df['value'].min()
    max_val = df['value'].max()
    unit = df['unit'].iloc[0] if len(df) > 0 and pd.notna(df['unit'].iloc[0]) else ''

    width_inches = args.width / 100
    height_inches = args.height / 100

    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=100)
    ax.plot(df['timestamp'], df['value'], linewidth=1, label='Value')

    ax.set_xlabel('Time')
    ax.set_ylabel(f'Value ({unit})' if unit else 'Value')
    ax.set_title(f'{args.sensor_name} - {args.type}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(args.output, dpi=100)
    plt.close()

    print(f'Chart saved to {args.output}')
    print(f'Min: {min_val}, Max: {max_val}, Points: {len(df)}')


if __name__ == '__main__':
    main()