import gpxpy
import gpxpy.gpx
import pytz
from datetime import datetime, timedelta


def update_gpx_timestamps(input_file, output_file, new_start_time):
    with open(input_file, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Calculate time difference between old start time and new start time
    original_time = gpx.tracks[0].segments[0].points[0].time
    time_diff = new_start_time - original_time

    # Update timestamps for all track points
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point.time = point.time + time_diff

    # Save the updated GPX file
    with open(output_file, "w") as new_gpx_file:
        new_gpx_file.write(gpx.to_xml())


if __name__ == "__main__":
    # Input and output GPX file paths
    input_gpx = "Afternoon_Ride.gpx"
    output_gpx = "output.gpx"

    # New start date and time (replace with your desired date/time)
    new_start_time = datetime(2024, 9, 7, 15, 12, 0)

    # set timezone to Warsaw
    timezone = pytz.timezone("Europe/Warsaw")
    new_start_time = timezone.localize(new_start_time)
update_gpx_timestamps(input_gpx, output_gpx, new_start_time)
