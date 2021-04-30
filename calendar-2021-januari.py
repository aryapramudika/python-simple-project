#Mengimport modul calendar
import calendar

#Mendefinisikan variabel jan sebagai kalender berbasis text yang diawali dengan hari Sunday (Minggu)
jan=calendar.TextCalendar(calendar.SUNDAY)
#Mencetak kalender berdasarkan bulan dengan prmont dengan format (tahun, bulan)
jan.prmonth(2021, 1)

