'''
Created on 6 Jan 2015

@author: chris
'''
def main():
    from oldschoolsql import login
    
    cur, mysql_cn = login()
    
    search_str = 'SELECT name FROM countries'
    
    cur.execute(search_str)
    results = cur.fetchall()
    
    mysql_cn.commit()
    mysql_cn.close()
    
    for result in results:
        print result

if __name__ == '__main__':
    main()