# this is for dev pc only and MySQL
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass