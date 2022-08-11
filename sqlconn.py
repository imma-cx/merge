import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=EMANUELR-LT;"
                      "Database=CxDB;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('select [Id],[FullName],[Name],[ParentId],[TenantId],[CreationDate] from accesscontrol.teams')

for row in cursor:
    print('row = %r' % (row,))

    #SQL Server
    #SQL Server Native Client 11.0