marker_count = 14

if __name__ == '__main__':
    data = open('input.txt').read()
  
    for i in range(0, (len(data)-marker_count+1)):
        temp = data[i:i+marker_count]
        if len(set(temp)) == len(temp):
            print("Marker Position",i+marker_count)
            break