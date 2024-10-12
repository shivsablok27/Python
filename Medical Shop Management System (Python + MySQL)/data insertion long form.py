import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="holy")
mycursor=mydb.cursor()
st="Insert into MEDICAL Values("\
+str(1810) +","+ "'CETIRIZINE'"     + ","+"'Anti-Alergic'"     +","+"'Sun Pharma'"      +"," +"'Tablet'"    +","+str(50.00)+","+"'2024-01-01'"  +")" + ",("\
+str(1811) +","+ "'CINNARIZINE'"    + ","+"'Anti-Alergic'"     +","+"'Cipla'"           +"," +"'Tablet'"    +","+str(55.00)+","+"'2025-02-02'"  +")" + ",("\
+str(1812) +","+ "'LEVOCETIRIZINE'" + ","+"'Anti-Alergic'"     +","+"'Cipla'"           +"," +"'Syrup'"     +","+str(90.00)+","+"'2026-03-31'"  +")" + ",("\
+str(1813) +","+ "'THEOPHYLLINE'"    +","+ "'Anti-Asthamatic'" +","+"'Dr. Reddy'"       +"," +"'Tablet'"    +","+str(45.00)+","+"'2023-04-28'"  +")" + ",("\
+str(1814) +","+ "'AZITHROMYCIN'"    +","+ "'Anti-biotic'"     +"," +"'Cipla'"          +"," +"'Suspension'" +","+str(37.00)+","+"'2023-05-17'"  +")" + ",("\
+str(1815) +","+ "'CEFUROXIME'"      +","+ "'Anti-biotic'"     +"," +"'Cipla'"          +"," +"'Tablet'"    +","+str(75.00)+","+"'2025-06-19'"  +")" + ",("\
+str(1816) +","+ "'CEFIXIME'"        +","+ "'Anti-biotic'"     +"," +"'Sun Pharma'"     +"," +"'Syrup'"      +","+str(92.00)+","+"'2022-12-16'"  +")" + ",("\
+str(1817) +","+ "'AMOXYCILLIN'"     +","+ "'Anti-biotic'"     +"," +"'Cipla'"          +"," +"'Capsules'"   +","+str(67.00)+","+"'2022-11-14'"  +")" + ",("\
+str(1818) +","+ "'MUPIROCIN'"       +","+ "'Anti-biotic'"     +"," +"'Histashield'"    +"," +"'Ointment'"   +","+str(87.00)+","+"'2025-09-12'"  +")" + ",("\
+str(1819) +","+ "'PARACETAMOL'"     +","+ "'Anti-cold'"       +"," +"'Histashield'"    +"," +"'Tablet'"    +","+str(56.00)+","+"'2024-03-12'"  +")" + ",("\
+str(1820) +","+ "'PHENYLEPHRINE'"   +","+ "'Anti-cold'"       +"," +"'Dr. Reddy'"      +"," +"'Syrup'"      +","+str(87.00)+","+"'2024-09-30'"  +")" + ",("\
+str(1821) +","+ "'VOGLIBOSE'"       +","+ "'Anti-Diabetic'"   +"," +"'Cipla'"          +"," +"'Tablet'"    +","+str(77.00)+","+"'2024-10-30'"  +")" + ",("\
+str(1822) +","+ "'METFORMIN'"       +","+ "'Anti-Diabetic'"   +"," +"'Cipla'"          +"," +"'Tablet'"    +","+str(75.00)+","+"'2023-10-20'"  +")" + ",("\
+str(1823) +","+ "'LULICONAZOLE'"    +","+ "'Anti-fungal'"     +"," +"'Life Shield'"    +"," +"'Spray'"      +","+str(99.00)+","+"'2026-10-09'"  +")" + ",("\
+str(1824) +","+ "'KETOCONAZOLE'"    +","+ "'Anti-fungal'"     +"," +"'Cipla'"          +"," +"'Shampoo'"    +","+str(39.00)+","+"'2025-07-13'"  +")" + ",("\
+str(1825) +","+ "'PANTOPRAZOLE'"    +","+ "'Anti-ulcerant'"   +"," +"'Mankind Pharma'" +"," +"'Injection'"  +","+str(95.00)+","+"'2024-08-27'"  +")" + ",("\
+str(1826) +","+ "'CURCUMIN'"        +","+ "'Anti-Viral'"      +"," +"'Mankind Pharma'" +"," +"'Powder'"    +","+str(98.00)+","+"'2022-12-14'"  +")" + ",("\
+str(1827) +","+ "'DICYCLOMINE'"     +","+ "'Pain-management'" +"," +"'Sun Pharma'"     +"," +"'Drops'"      +","+str(50.00)+","+"'2024-04-22'"  +")" + ",("\
+str(1828) +","+ "'PIROXICAM'"       +","+"'Analgesic'"        +"," +"'Mankind Pharma'" +"," +"'Ointment'"  +","+str(86.00)+","+"'2025-05-29'"  +")" + ",("\
+str(1829) +","+ "'PIROXICAM'"       +","+"'Analgesic'"        +"," +"'Mankind Pharma'" +"," +"'Ointment'"  +","+str(86.00)+","+"'2025-05-29'"  + ")" 
mycursor.execute (st)
mydb.commit()
mydb.close()
