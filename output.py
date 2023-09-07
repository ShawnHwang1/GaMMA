catalog_start_time = '2022-12-20T00:00:00'

fout = open(catalog, 'w')
with open(catalog, 'r') as fin:
    for line in fin:
        split_line = line.split()
        year = int(split_line[0])
        month = int(split_line[1])
        day = int(split_line[2])
        hour = int(split_line[3])
        minute = int(split_line[4])
        second = float(split_line[5])
        if (second >= 60.0):
            print("BEFORE: ", year, month, day, hour, minute, second)
            second -= 60.0
            minute += 1
            print("AFTER: ", year, month, day, hour, minute, second)
fout = open(catalog, 'w')
fout_nonclust = open(out_nonclust_file, 'w')
with open(catalog, 'r') as fin:
    for line in fin:
        split_line = line.split()
        year = int(split_line[0])
        month = int(split_line[1])
        day = int(split_line[2])
        hour = int(split_line[3])
        minute = int(split_line[4])
        second = float(split_line[5])
        if (second >= 60.0):
            print("BEFORE: ", year, month, day, hour, minute, second)
            second -= 60.0
            minute += 1
            print("AFTER: ", year, month, day, hour, minute, second)
        origin_time_nosec = datetime.datetime(year, month, day, hour, minute)
        origin_delta = datetime.timedelta(seconds=second)
        origin_time = origin_time_nosec + origin_delta
        origin_str = datetime.datetime.strftime(origin_time, '%Y-%m-%dT%H:%M:%S.%f')
        longitude = split_line[10]
        latitude = split_line[11]
        depth_km = split_line[12]
        evid = int(split_line[7])
        fout.write(("%s %f %s %s %s %s %d\n") % (origin_str, num_sec, longitude, latitude, depth_km, evid))
        fout.write(("%f %s %s %s %s %d\n") % (num_sec, longitude, latitude, depth(km), evid))
fout_nonclust.write(("%s %f %s %s %s %s %d\n") % (origin_str, num_sec, lat_deg, lon_deg, depth_km, evid))
fout_nonclust.write(("%f %s %s %s %s %d\n") % (longitude, latitude, depth_km, evid))
fout.close()
fout_nonclust.close()