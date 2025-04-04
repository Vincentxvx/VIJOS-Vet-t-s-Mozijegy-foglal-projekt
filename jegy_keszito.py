def jegy():
    #Importálások (pdf, mysql)
    from fpdf import FPDF
    import mysql.connector
    
    #Adatbázis kapcsolása
    # kapcsolat = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="",
    #         database="mozijegy"
    #     )
    # cursor = kapcsolat.cursor()
    
    #Adatok kinyerése
    
    # cursor.execute("SELECT * FROM foglalo WHERE foglalo.foglaloID = 8")
    # result = cursor.fetchone()
    # vnev = result[0]
    # knev = result[1]
    mozijegy = FPDF('P', 'mm', 'A4')
    mozijegy.add_page()
    
    #Keret és elválasztó vonalak tulajdonságai
    mozijegy.set_draw_color(225, 165, 0)
    mozijegy.set_line_width(5)
    
    #Keret
    mozijegy.line(0, 1, 210, 2)
    mozijegy.line(0, 1, 0, 400)
    mozijegy.line(210, 1, 210, 400)
    mozijegy.line(0, 295, 210, 295)
    
    #Elválasztó vonalak
    mozijegy.line(0, 225, 210, 225)
    mozijegy.set_line_width(1)
    mozijegy.line(0+17, 40, 210-17, 40)
    mozijegy.line(0+17, 100, 210-17, 100)
    mozijegy.line(0+17, 175, 210-17, 175)
    mozijegy.line(0+17, 200, 210-17, 200)

    
    #Szövegek + képek
    mozijegy.image('./VIJOS-Vet-t-s-Mozijegy-foglal-projekt/images/qr-code.png', x=135, y=105, h=60, w=60, type="PNG")
    mozijegy.set_text_color(225, 165, 0)
    mozijegy.set_font(family="Arial", style="B", size=32.5)
    mozijegy.text(x=17, y=117.5, text="TEREM")
    mozijegy.text(x=17, y=137.5, text="SOR")
    mozijegy.text(x=17, y=157.5, text="SZÉK")
    mozijegy.set_text_color(0, 0, 0)
    
    mozijegy.text(x=75, y=117.5, text="3. terem,")
    mozijegy.text(x=75, y=137.5, text="2")
    mozijegy.text(x=75, y=157.5, text="10")
    
    mozijegy.set_text_color(225, 165, 0)
    mozijegy.set_font(family="Arial", style="B", size=23.5)
    mozijegy.text(x=15, y=20, text="VÁSÁRLÁS")
    mozijegy.text(x=15, y=30, text="AZONOSÍTÓ")

    mozijegy.set_text_color(0, 0, 0)
    mozijegy.set_font(family="Arial", style="", size=23.5)
    mozijegy.text(x=90.25, y=30, text="577635437")
    mozijegy.image('./VIJOS-Vet-t-s-Mozijegy-foglal-projekt/images/popcorn.png', x=140, y=12.5, h=30, w=30, type="PNG")
    mozijegy.image('./VIJOS-Vet-t-s-Mozijegy-foglal-projekt/images/soda.png', x=155.5, y=7.5, h=40, w=40, type="PNG")
    
    mozijegy.set_text_color(225, 165, 0)
    mozijegy.set_font(family="Arial", style="B", size=23.5)
    mozijegy.text(x=15, y=52.5, text="ELÖADÁS")
    
    mozijegy.set_text_color(0, 0, 0)
    mozijegy.set_font(family="Arial", style="", size=23.5)
    mozijegy.text(x=75, y=52.5, text="(HU/mb) Deadpool & Rozsomák")
    mozijegy.text(x=15, y=67.5, text="vasárnap 2024.08.04 19:15")
    mozijegy.text(x=15, y=82.5, text="Vincent-Patrik-Lajos Cinema")

    mozijegy.set_font(family="Arial", style="", size=17.5)
    mozijegy.text(x=15, y=185, text="Diákjegy")
    mozijegy.text(x=75, y=185, text="1131334647402001")
    mozijegy.text(x=150, y=185, text="2 100.00 Ft")
    
    mozijegy.set_font(family="Arial", style="B", size=12.5)
    mozijegy.text(x=15, y=240, text="CÉGNÉV:")
    mozijegy.text(x=15, y=250, text="SZÉKHELY:")
    mozijegy.text(x=15, y=260, text="ADÓSZÁM:")
    
    mozijegy.set_text_color(225, 165, 0)
    mozijegy.text(x=45, y=240, text="Vincent-Patrik-Lajos Cinema Kft.")
    mozijegy.text(x=45, y=250, text="8200. Veszprém Iskola utca 4.")
    mozijegy.text(x=45, y=260, text="8511670549")
    mozijegy.image('./VIJOS-Vet-t-s-Mozijegy-foglal-projekt/images/logo.png', x=150, y=227.1234321343212454322456321, h=40, w=40, type="PNG")
    
    mozijegy.set_font(family="Arial", style="B", size=15)
    mozijegy.text(x=10.5, y=272.5, text="KÖSZÖNJÜK, HOGY A VINCENT-PATRIK-LAJOS CINEMA-BAN MOZIZOL! :)")
    mozijegy.text(x=27.5, y=280, text="JÓ SZÓRAKOZÁST, KELLEMES MOZIÉLMÉNYT KÍVÁNUNK!")

    
    mozijegy.output('mozijegy.pdf')
    
jegy()