from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

def checking (a):
    se = set()
    for i in range (3):
        for j in range (3):
            se.add(a[i][j])
        if (len(se) == 1):
            return True
        else:
            se = set()
    for i in range(3):
        for j in range (3):
            se.add(a[j][i])
        if (len(se) == 1):
            return True
        else:
            se = set()
    for i in range (3):
        se.add(a[i][i])
    if (len(se) == 1):
        return True
    else:
        se = set()
    for i in range (3):
        se.add(a[i][3 - i - 1])
    if (len(se) == 1):
        return True

def vtroiky(a):
    x = int(a)
    s = ""
    while x != 0:
        s = s + str(x % 3)
        x = x // 3
    s = s[::-1]
    while (len(s) != 2):
        s = "0" + s
    return s


matrix = [["2", "3", "4"], ["5", "6", "7"], ["8", "9", "10"]]
a = -1
lab = Label(text="Ходят крестики")


class CrossZero(App):
    def build(self):
        gl = GridLayout(cols=3)
        bl = BoxLayout(orientation="horizontal")
        self.knopka = []
        for i in range(1, 10):
            self.knopka.append(Button(
                on_press = self.callback_press,
                background_color = (255, 255, 255, 1),
                id = str(i - 1)
            ))
            gl.add_widget(self.knopka[i - 1])
        bl.add_widget(gl)
        bl.add_widget(lab)
        return bl

    def callback_press(self, instance):
        global a
        global lab
        if ((instance.text=="") and (lab.text!="Ничья") and (lab.text!="Победили нолики") and (lab.text!="Победили крестики")):
            a += 1
            return self.callback_release(instance, a, lab)

    def callback_release(self, instance, a, lab):
        global matrix
        if (a % 2 == 0):
            instance.text="x"
            instance.background_color = (1, 1, 1, 1)
            x = vtroiky(instance.id)
            matrix[int(x[0])][int(x[1])] = 1
            if (checking(matrix) == True):
                lab.text="Победили крестики"
            elif (a == 8):
                lab.text="Ничья"
            else:
                lab.text="Ходят нолики"
        else:
            instance.text="o"
            instance.background_color = (1, 1, 1, 1)
            x = vtroiky(instance.id)
            matrix[int(x[0])][int(x[1])] = 0
            if (checking(matrix) == True):
                lab.text="Победили нолики"
            elif (a == 8):
                lab.text="Ничья"
            else:
                lab.text="Ходят крестики"

if __name__ == "__main__":
    CrossZero().run()