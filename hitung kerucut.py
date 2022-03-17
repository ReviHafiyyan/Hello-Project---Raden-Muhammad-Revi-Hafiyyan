'''sebuah program yang akan menghitung volume dari sebuah kerucut terpancung.
Masukan berupa 3 baris: r, R, dan t.
Luas Selimut Kerucut Terpancung = pi*s (R+r)
Volume Kerucut Terpancung = (pi*t)/3 (R**2 + Rr + r**2)

Cetak jawaban dalam 2 angka di belakang koma.

*gunakan pi = 3.14'''

pi = 3.14

def volume(r, R, t):
    return pi*t*(R*R + R*r + r*r)/3

r = int(input())
R = int(input())
t = int(input())
print ("{:.2f}".format(volume(r, R, t)))
