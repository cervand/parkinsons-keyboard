import pymysql

db = pymysql.connect(host='localhost',
    user = 'mp2',
    passwd = 'eecs116',
    db = 'blurts')
cur = db.cursor()



def queryOne():
    sql = "SELECT topic.id, topic.description, COUNT(blurt_analysis.blurtid) FROM blurt_analysis, topic WHERE topic.id= blurt_analysis.topicid GROUP BY topicid ORDER BY topicid;"
    cur.execute(sql) 

    for row in cur.fetchall(): # cur.fetchone() gets one result at a time 
        print(row) 


def queryTwo():
    sql = "SELECT user.name, count(follow.follower) FROM follow, celebrity, user WHERE follow.followee = user.email AND follow.followee = celebrity.email GROUP BY follow.followee;"
    cur.execute(sql) 

    for row in cur.fetchall(): # cur.fetchone() gets one result at a time 
        print(row) 

def queryThree():
    sql = "SELECT user.name, count(blurt.email) FROM blurt, celebrity, user WHERE blurt.email = celebrity.email AND user.email = celebrity.email GROUP BY user.name ORDER BY count(blurt.email) DESC;"
    cur.execute(sql) 

    for row in cur.fetchall(): # cur.fetchone() gets one result at a time 
        print(row) 

queryOne()
print("\n")
queryTwo()
print("\n")
queryThree()

db.close()