def jegy():
    #Importálások (pdf, mysql)
    from fpdf import FPDF
    import mysql.connector
    
    #Adatbázis kapcsolása
    kapcsolat = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mozijegy"
        )
    cursor = kapcsolat.cursor()
    
    #Adatok kinyerése
    
    cursor.execute("SELECT * FROM foglalo WHERE foglalo.foglaloID = 20")
    result = cursor.fetchone()
    vnev = result[0]
    knev = result[1]
    mozijegy = FPDF('P', 'mm', 'A4')
    mozijegy.add_page()
    mozijegy.set_font('times', '', 16)
    mozijegy.cell(40, 40, f'{vnev} {knev}')
    
    mozijegy.output('mozijegy.pdf')
    
jegy()