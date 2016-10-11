import json



def checkPrice(threshold,data):
    print " PRICES"
    #threshold=[1000,1500,2000]
    courses=[0,0,0,0]
    fullcourses=[[],[],[],[]]
    unknown=0
    for course in data:
        if course['price']:
            try:
                price=int(course['price'].replace('.',''))
                i=0
                found=False
                for t in threshold:
                    if(price<=t):
                        fullcourses[i].append(course)
                        courses[i]=courses[i]+1
                        found=True
                        break
                    i=i+1
                if not found:
                    courses[i]=courses[i]+1
                    fullcourses[i].append(course)
            except ValueError:
                unknown=unknown+1
    print len(data)
    for c in courses:
        print c
    print unknown

    for i in xrange(0,len(threshold)):
        print "PRICE under "+str(threshold[i])+"\t perc:"+str(courses[i]*100./len(data))
    print "PRICE over "+str(threshold[i])+"\t\t perc:"+str(courses[i+1]*100./len(data))
    print "unknow \t\t\tperc:"+str(unknown*100./len(data))
    return


def checkHours(threshold,data,country):
    replacer={"IT":" ore di lezione","DE":" Lehrstunden","FR":" heures de formation","ES":" horas lectivas"}
    print " HOURS"
    #threshold=[16,24,36,48]
    courses=[0,0,0,0,0]
    unknown=0
    z=0
    for course in data:
        if course['hours']:
            z=z+1
            try:
                h=course['hours'].replace(replacer[country],'')
                h=int(h)
                i=0
                found=False
                for t in threshold:
                    if(h<=t):
                        courses[i]=courses[i]+1
                        found=True
                        break
                    i=i+1
                if not found:
                    courses[i]=courses[i]+1
            except ValueError:
               unknown=unknown+1
        else:
            unknown=unknown+1
    print z
    for c in courses:
        print c
    print unknown

    for i in xrange(0,len(threshold)):
        print "hours under "+str(threshold[i])+"\t perc:"+str(courses[i]*100./len(data))
    print "hours over "+str(threshold[i])+"\t perc:"+str(courses[i+1]*100./len(data))
    print "unknow \t\t\tperc:"+str(unknown*100./len(data))


with open('corsiES.json') as data_file:
        dd = json.load(data_file)
checkPrice([1000,1500,2000],dd)
checkHours([16,24,36,48],dd,"ES")