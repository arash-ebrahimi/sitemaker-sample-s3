from django import forms

class About1(forms.Form):
    c1 = forms.CharField(required=False)
    c2 = forms.CharField(required=False)
    c3 = forms.CharField(required=False)
    c4 = forms.CharField(widget=forms.Textarea,   required=False)
    c5 = forms.CharField(required=False)
    c6 = forms.CharField(required=False)
    c7 = forms.CharField(required=False)
    c8 = forms.CharField(required=False)
    c9 = forms.CharField(required=False)
    c10 = forms.CharField(required=False)
    c11 = forms.CharField(required=False)
    c12 = forms.CharField(required=False)
    c13 = forms.CharField(required=False)
    c14 = forms.CharField(required=True)
    c15 = forms.CharField(required=True)
    c16 = forms.CharField(required=False)
    c17 = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['c8','c9','c10','c11','c16','c17']
        link = ['c14','c15']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class About4(forms.Form):
    c1 = forms.CharField(required=False)
    c2 = forms.CharField(required=False)
    c3 = forms.CharField(required=False)
    c4 = forms.CharField(widget=forms.Textarea,   required=False)
    c5 = forms.CharField(required=False)
    c6 = forms.CharField(required=False)
    c7 = forms.CharField(required=False)
    c13 = forms.CharField(required=False)
    c14 = forms.CharField(required=True)


    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =[]
        link = ['c14']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Featured1(forms.Form):
    c1 = forms.CharField(required=False)
    c2 = forms.CharField(required=False)
    c3 = forms.CharField(required=False)
    c4 = forms.CharField(required=False)
    c5 = forms.CharField(required=False)
    c6 = forms.CharField(required=False)
    c7 = forms.CharField(required=False)
    c8 = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['c7','c8']
        link = []
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class About2(forms.Form):
    c1 = forms.CharField(required=False)
    c2 = forms.CharField(required=False)
    c3 = forms.CharField(required=False)
    c4 = forms.CharField(required=False)
    c5 = forms.CharField(required=False)
    c6 = forms.CharField(required=False)
    c7 = forms.IntegerField(required=False)
    c7_from100 = forms.IntegerField(required=False)
    c8 = forms.IntegerField(required=False)
    c8_from100 = forms.IntegerField(required=False)
    c9 = forms.IntegerField(required=False)
    c9_from100 = forms.IntegerField(required=False)
    c10 = forms.CharField(required=False)
    c11 = forms.CharField(required=False)
    c12 = forms.CharField(required=False)
    c13 = forms.CharField(required=False)
    c14 = forms.IntegerField(required=False)
    c15 = forms.IntegerField(required=False)
    c16 = forms.IntegerField(required=False)
    c17 = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['c11','c12','c13']
        link = ['c17']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Callaction1(forms.Form):
    c1 = forms.CharField(required=False)
    c2 = forms.CharField(required=False)
    c3 = forms.CharField(required=False)
    c4 = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['c3']
        link = ['c4']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Cases1(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    c1_1 = forms.CharField(required=False)
    c1_2 = forms.CharField(required=False)
    c1_IMG = forms.CharField(required=False)
    c1_REF = forms.CharField(required=False)
    c2_1 = forms.CharField(required=False)
    c2_2 = forms.CharField(required=False)
    c2_IMG = forms.CharField(required=False)
    c2_REF = forms.CharField(required=False)
    c3_1 = forms.CharField(required=False)
    c3_2 = forms.CharField(required=False)
    c3_IMG = forms.CharField(required=False)
    c3_REF = forms.CharField(required=False)
    c4_1 = forms.CharField(required=False)
    c4_2 = forms.CharField(required=False)
    c4_IMG = forms.CharField(required=False)
    c4_REF = forms.CharField(required=False)
    c5_1 = forms.CharField(required=False)
    c5_2 = forms.CharField(required=False)
    c5_IMG = forms.CharField(required=False)
    c5_REF = forms.CharField(required=False)
    f_1 = forms.CharField(required=False)
    b = forms.CharField(required=False)
    b_REF = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['c1_IMG','c2_IMG','c3_IMG','c4_IMG','c5_IMG']
        link = ['c1_REF','c2_REF','c3_REF','c4_REF','c5_REF','b_REF']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Cases2(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    c1_1 = forms.CharField(required=False)
    c1_2 = forms.CharField(required=False)
    c1_IMG = forms.CharField(required=False)
    c1_REF = forms.CharField(required=False)
    c2_1 = forms.CharField(required=False)
    c2_2 = forms.CharField(required=False)
    c2_IMG = forms.CharField(required=False)
    c2_REF = forms.CharField(required=False)
    c3_1 = forms.CharField(required=False)
    c3_2 = forms.CharField(required=False)
    c3_IMG = forms.CharField(required=False)
    c3_REF = forms.CharField(required=False)
    c4_1 = forms.CharField(required=False)
    c4_2 = forms.CharField(required=False)
    c4_IMG = forms.CharField(required=False)
    c4_REF = forms.CharField(required=False)
    c5_1 = forms.CharField(required=False)
    c5_2 = forms.CharField(required=False)
    c5_IMG = forms.CharField(required=False)
    c5_REF = forms.CharField(required=False)
    f_1 = forms.CharField(required=False)
    b = forms.CharField(required=False)
    b_REF = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['c1_IMG','c2_IMG','c3_IMG','c4_IMG','c5_IMG']
        link = ['c1_REF','c2_REF','c3_REF','c4_REF','c5_REF','b_REF']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Counter1(forms.Form):
    c1 = forms.CharField(required=False)
    c1_VAL =  forms.CharField(required=False)
    c2 = forms.CharField(required=False)
    c2_VAL = forms.CharField(required=False)
    c3 = forms.CharField(required=False)
    c3_VAL = forms.CharField(required=False)
    c4 = forms.CharField(required=False)
    c4_VAL = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =[]
        link = []
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Detail1(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    IMG = forms.CharField(required=False)
    Card_TITLE = forms.CharField(required=False)
    Card_TEXT = forms.CharField(widget=forms.Textarea,   required=False)
    item1 = forms.CharField(required=False)
    Value1 = forms.CharField(required=False)
    item2 = forms.CharField(required=False)
    Value2 = forms.CharField(required=False)
    item3 = forms.CharField(required=False)
    Value3 = forms.CharField(required=False)
    item4= forms.CharField(required=False)
    Value4 = forms.CharField(required=False)
    item5 = forms.CharField(required=False)
    Value5 = forms.CharField(required=False)
    T_1 = forms.CharField(required=False)
    TX_1 = forms.CharField(widget=forms.Textarea,   required=False)
    T_2 = forms.CharField(required=False)
    TX_2 = forms.CharField(widget=forms.Textarea, required=False)
    T_3 = forms.CharField(required=False)
    TX_3 = forms.CharField(widget=forms.Textarea, required=False)
    b1 = forms.CharField(required=False)
    b1_REF = forms.CharField(required=True)
    b2 = forms.CharField(required=False)
    b2_REF = forms.CharField(required=True)

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        image =['IMG']
        link = ['b1_REF','b2_REF']
        for myField in self.fields:
            self.fields[myField].widget.attrs['dir'] = 'rtl'
            self.fields[myField].widget.attrs['style'] ='width: auto;'
            if myField in image:
                self.fields[myField].widget.attrs['style'] += 'color:red'
            if myField in link:
                self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Detail2(forms.Form):
    h1 = forms.CharField(required=False)
    T_1 = forms.CharField(required=False)
    TX_1 = forms.CharField(widget=forms.Textarea,   required=False)
    T_2 = forms.CharField(required=False)
    TX_2 = forms.CharField(widget=forms.Textarea, required=False)
    T_3 = forms.CharField(required=False)
    TX_3 = forms.CharField(widget=forms.Textarea, required=False)
    help_1 = forms.CharField(required=False)
    help_2 = forms.CharField(widget=forms.Textarea,   required=False)
    help_3 = forms.CharField(required=False)
    help_4 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    Item_1 = forms.CharField(required=False)
    Item_2 = forms.CharField(required=False)
    Item_3 = forms.CharField(required=False)
    Item_4 = forms.CharField(required=False)
    Item_5 = forms.CharField(required=False)
    Item_6 = forms.CharField(required=False)
    Item1_REF = forms.CharField(required=True)
    Item2_REF = forms.CharField(required=True)
    Item3_REF = forms.CharField(required=True)
    Item4_REF = forms.CharField(required=True)
    Item5_REF = forms.CharField(required=True)
    Item6_REF = forms.CharField(required=True)
    Item1_SEL = forms.CharField(required=False)
    Item2_SEL = forms.CharField(required=False)
    Item3_SEL = forms.CharField(required=False)
    Item4_SEL = forms.CharField(required=False)
    Item5_SEL = forms.CharField(required=False)
    Item6_SEL = forms.CharField(required=False)
    iconmain = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2']
            link = ['Item1_REF','Item2_REF','Item3_REF',
                    'Item4_REF','Item5_REF','Item6_REF']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Detail3(forms.Form):
    h1 = forms.CharField(required=False)
    T_1 = forms.CharField(required=False)
    TX_1 = forms.CharField(widget=forms.Textarea,   required=False)
    T_2 = forms.CharField(required=False)
    TX_2 = forms.CharField(widget=forms.Textarea, required=False)
    T_3 = forms.CharField(required=False)
    TX_3 = forms.CharField(widget=forms.Textarea, required=False)
    help_1 = forms.CharField(required=False)
    help_2 = forms.CharField(widget=forms.Textarea,   required=False)
    help_3 = forms.CharField(required=False)
    help_4 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    Item_1 = forms.CharField(required=False)
    Item_2 = forms.CharField(required=False)
    Item_3 = forms.CharField(required=False)
    Item_4 = forms.CharField(required=False)
    Item_5 = forms.CharField(required=False)
    Item_6 = forms.CharField(required=False)
    Item1_REF = forms.CharField(required=True)
    Item2_REF = forms.CharField(required=True)
    Item3_REF = forms.CharField(required=True)
    Item4_REF = forms.CharField(required=True)
    Item5_REF = forms.CharField(required=True)
    Item6_REF = forms.CharField(required=True)
    Item1_SEL = forms.CharField(required=False)
    Item2_SEL = forms.CharField(required=False)
    Item3_SEL = forms.CharField(required=False)
    Item4_SEL = forms.CharField(required=False)
    Item5_SEL = forms.CharField(required=False)
    Item6_SEL = forms.CharField(required=False)
    iconmain = forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    T4 = forms.CharField(required=False)
    H5 = forms.CharField(required=False)
    T5 = forms.CharField(required=False)
    H6 = forms.CharField(required=False)
    T6 = forms.CharField(required=False)
    H7 = forms.CharField(required=False)
    T7 = forms.CharField(required=False)
    H8 = forms.CharField(required=False)
    T8 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2']
            link = ['Item1_REF','Item2_REF','Item3_REF',
                    'Item4_REF','Item5_REF','Item6_REF']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Detail4(forms.Form):
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    T4 = forms.CharField(required=False)
    H5 = forms.CharField(required=False)
    T5 = forms.CharField(required=False)
    H6 = forms.CharField(required=False)
    T6 = forms.CharField(required=False)
    H7 = forms.CharField(required=False)
    T7 = forms.CharField(required=False)
    H8 = forms.CharField(required=False)
    T8 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Experience1(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    Item1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    Item2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    Item3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    Item4 = forms.CharField(required=False)
    H5 = forms.CharField(required=False)
    Item5 = forms.CharField(required=False)
    Item1_H = forms.CharField(required=False)
    Item1_T = forms.CharField(required=False)
    Item1_B = forms.CharField(required=False)
    Item1_REF = forms.CharField(required=False)
    Item2_H = forms.CharField(required=False)
    Item2_T = forms.CharField(required=False)
    Item2_B = forms.CharField(required=False)
    Item2_REF = forms.CharField(required=False)
    Item3_H = forms.CharField(required=False)
    Item3_T = forms.CharField(required=False)
    Item3_B = forms.CharField(required=False)
    Item3_REF = forms.CharField(required=False)
    Item4_H = forms.CharField(required=False)
    Item4_T = forms.CharField(required=False)
    Item4_B = forms.CharField(required=False)
    Item4_REF = forms.CharField(required=False)
    Item5_H = forms.CharField(required=False)
    Item5_T = forms.CharField(required=False)
    Item5_B = forms.CharField(required=False)
    Item5_REF = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = ['Item1_REF','Item2_REF','Item3_REF',
                    'Item4_REF','Item5_REF']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class faq1(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    RIGHT_1_Q = forms.CharField(required=False)
    RIGHT_1_A = forms.CharField(required=False)
    RIGHT_2_Q = forms.CharField(required=False)
    RIGHT_2_A = forms.CharField(required=False)
    RIGHT_3_Q = forms.CharField(required=False)
    RIGHT_3_A = forms.CharField(required=False)
    RIGHT_4_Q = forms.CharField(required=False)
    RIGHT_4_A = forms.CharField(required=False)
    RIGHT_5_Q = forms.CharField(required=False)
    RIGHT_5_A = forms.CharField(required=False)
    LEFT_1_Q = forms.CharField(required=False)
    LEFT_1_A = forms.CharField(required=False)
    LEFT_2_Q = forms.CharField(required=False)
    LEFT_2_A = forms.CharField(required=False)
    LEFT_3_Q = forms.CharField(required=False)
    LEFT_3_A = forms.CharField(required=False)
    LEFT_4_Q = forms.CharField(required=False)
    LEFT_4_A = forms.CharField(required=False)
    LEFT_5_Q = forms.CharField(required=False)
    LEFT_5_A = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Fluid1(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    TXT = forms.CharField(widget=forms.Textarea,   required=False)
    Item1 = forms.CharField(required=False)
    Value1 = forms.CharField(required=False)
    Item2 = forms.CharField(required=False)
    Value2 = forms.CharField(required=False)
    Item3 = forms.CharField(required=False)
    Value3 = forms.CharField(required=False)
    IMG_Pattern = forms.CharField(required=False)
    BG_IMG = forms.CharField(required=False)
    IMG_Main = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG_Pattern','IMG_Main','BG_IMG']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Fluid2(forms.Form):
    h1 = forms.CharField(required=False)
    h2 = forms.CharField(required=False)
    TXT = forms.CharField(widget=forms.Textarea,   required=False)

    IMG_Pattern = forms.CharField(required=False)
    BG_IMG = forms.CharField(required=False)
    IMG_Main = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG_Pattern','IMG_Main','BG_IMG']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Header1(forms.Form):
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    TXT1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    TXT2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    TXT3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)




    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3']
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Header2(forms.Form):
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    TXT1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    TXT2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    TXT3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3']
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Header3(forms.Form):
    H1 = forms.CharField(required=False)
    TXT1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    TXT2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    TXT3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    PATTERN1 = forms.CharField(required=False)
    PATTERN2 = forms.CharField(required=False)
    PATTERN3 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3']
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Header4(forms.Form):
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3']
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class News1(forms.Form):
    Header= forms.CharField(required=False)
    Title= forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    T4 = forms.CharField(widget=forms.Textarea, required=False)
    B4 = forms.CharField(required=False)
    REF4 = forms.CharField(required=False)
    H5 = forms.CharField(required=False)
    T5 = forms.CharField(widget=forms.Textarea, required=False)
    B5 = forms.CharField(required=False)
    REF5 = forms.CharField(required=False)
    H6 = forms.CharField(required=False)
    T6 = forms.CharField(widget=forms.Textarea, required=False)
    B6 = forms.CharField(required=False)
    REF6 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    IMG5 = forms.CharField(required=False)
    IMG6 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4','IMG5','IMG6',]
            link = ['REF1','REF2','REF3','REF4','REF5','REF6']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class News2(forms.Form):
    Header= forms.CharField(required=False)
    Title= forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    T4 = forms.CharField(widget=forms.Textarea, required=False)
    B4 = forms.CharField(required=False)
    REF4 = forms.CharField(required=False)

    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4']
            link = ['REF1','REF2','REF3','REF4']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Pricing1(forms.Form):
    Title1= forms.CharField(required=False)
    Title2= forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    P1 = forms.CharField(required=False)
    U1 = forms.CharField(required=False)
    B1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    Item1_1 = forms.CharField(required=False)
    Item1_2 = forms.CharField(required=False)
    Item1_3 = forms.CharField(required=False)
    Item1_4 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    P2 = forms.CharField(required=False)
    U2 = forms.CharField(required=False)
    B2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    Item2_1 = forms.CharField(required=False)
    Item2_2 = forms.CharField(required=False)
    Item2_3 = forms.CharField(required=False)
    Item2_4 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    P3 = forms.CharField(required=False)
    U3 = forms.CharField(required=False)
    B3 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    Item3_1 = forms.CharField(required=False)
    Item3_2 = forms.CharField(required=False)
    Item3_3 = forms.CharField(required=False)
    Item3_4 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Process1(forms.Form):
    Title1= forms.CharField(required=False)
    Title2= forms.CharField(required=False)
    S1 = forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    S2 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    B2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    S3 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    B3 = forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2']
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Services1(forms.Form):
    Title1= forms.CharField(required=False)
    Title2= forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    REF1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    REF2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    REF3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    T4 = forms.CharField(widget=forms.Textarea, required=False)
    REF4 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4']
            link = ['REF1','REF2','REF3','REF4']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Services2(forms.Form):
    Title1= forms.CharField(required=False)
    Title2= forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    REF1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    REF2 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    REF3 = forms.CharField(required=False)
    H4 = forms.CharField(required=False)
    T4 = forms.CharField(widget=forms.Textarea, required=False)
    REF4 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    PATTERN1 = forms.CharField(required=False)
    PATTERN2 = forms.CharField(required=False)
    PATTERN3 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4','PATTERN1','PATTERN2','PATTERN3']
            link = ['REF1','REF2','REF3','REF4']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Services3(forms.Form):
    N1 = forms.CharField(required=False)
    H1 = forms.CharField(required=False)
    T1 = forms.CharField(widget=forms.Textarea,   required=False)
    REF1 = forms.CharField(required=False)
    N2 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    T2 = forms.CharField(widget=forms.Textarea, required=False)
    REF2 = forms.CharField(required=False)
    N3 = forms.CharField(required=False)
    H3 = forms.CharField(required=False)
    T3 = forms.CharField(widget=forms.Textarea, required=False)
    REF3 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = ['REF1','REF2','REF3']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Shop1(forms.Form):
    Title1 = forms.CharField(required=False)
    Title2 = forms.CharField(required=False)
    Title3 = forms.CharField(required=False)
    Text1 = forms.CharField(widget=forms.Textarea,   required=False)
    Text2 = forms.CharField(widget=forms.Textarea, required=False)
    Text3 = forms.CharField(widget=forms.Textarea, required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Shop2(forms.Form):
    Title = forms.CharField(required=False)
    IMG = forms.CharField(required=False)
    MARGIN = forms.CharField(required=False)
    STAR = forms.CharField(required=False)
    PRICE = forms.CharField(required=False)
    TEXT = forms.CharField(widget=forms.Textarea,   required=False)
    B1 = forms.CharField(required=False)

    Item1 = forms.CharField(required=False)
    Value1 = forms.CharField(required=False)
    Item2 = forms.CharField(required=False)
    Value2 = forms.CharField(required=False)
    Item3 = forms.CharField(required=False)
    Value3 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Shop3(forms.Form):
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Sponsors1(forms.Form):
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    IMG5 = forms.CharField(required=False)
    IMG6 = forms.CharField(required=False)
    IMG7 = forms.CharField(required=False)
    IMG8 = forms.CharField(required=False)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4','IMG5','IMG6','IMG7','IMG8']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Sponsors2(forms.Form):
    IMG1 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    IMG5 = forms.CharField(required=False)
    IMG6 = forms.CharField(required=False)
    IMG7 = forms.CharField(required=False)
    IMG8 = forms.CharField(required=False)
    REF1 = forms.CharField(required=True)
    REF2 = forms.CharField(required=True)
    REF3 = forms.CharField(required=True)
    REF4 = forms.CharField(required=True)
    REF5 = forms.CharField(required=True)
    REF6 = forms.CharField(required=True)
    REF7 = forms.CharField(required=True)
    REF8 = forms.CharField(required=True)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4','IMG5','IMG6','IMG7','IMG8']
            link = ['REF1','REF2','REF3','REF4','REF5','REF6','REF7','REF8']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Team1(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(widget=forms.Textarea,   required=False)
    TEXT1 = forms.CharField(widget=forms.Textarea,   required=False)
    Name1 = forms.CharField(required=False)
    Title1 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    Title2 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    Name3 = forms.CharField(required=False)
    Title3 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    Name4 = forms.CharField(required=False)
    Title4 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    TEAM = forms.CharField(required=False)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4']
            link = ['TEAM']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Team2(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(widget=forms.Textarea,   required=False)
    TEXT1 = forms.CharField(widget=forms.Textarea,   required=False)
    Name1 = forms.CharField(required=False)
    Title1 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    Title2 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    Name3 = forms.CharField(required=False)
    Title3 = forms.CharField(required=False)
    IMG3 = forms.CharField(required=False)
    Name4 = forms.CharField(required=False)
    Title4 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    TEAM = forms.CharField(required=False)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4']
            link = ['TEAM']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Technology1(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(widget=forms.Textarea,   required=False)
    Name1 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    Name3 = forms.CharField(required=False)
    IMG3= forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    Name4 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    REF4 = forms.CharField(required=False)
    Name5 = forms.CharField(required=False)
    IMG5 = forms.CharField(required=False)
    REF5 = forms.CharField(required=False)
    BGIMG = forms.CharField(required=False)




    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4','IMG5','BGIMG']
            link = ['REF1','REF2','REF3','REF4','REF5']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Technology2(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    Name1 = forms.CharField(required=False)
    IMG1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    IMG2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)
    Name3 = forms.CharField(required=False)
    IMG3= forms.CharField(required=False)
    REF3 = forms.CharField(required=False)
    Name4 = forms.CharField(required=False)
    IMG4 = forms.CharField(required=False)
    REF4 = forms.CharField(required=False)
    BGIMG = forms.CharField(required=False)




    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2','IMG3','IMG4','BGIMG']
            link = ['REF1','REF2','REF3','REF4']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Testimonial1(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    Title1 = forms.CharField(widget=forms.Textarea, required=False)
    Name1 = forms.CharField(required=False)
    T1 = forms.CharField(required=False)
    TEXT1 = forms.CharField(widget=forms.Textarea, required=False)
    IMG1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    T2 = forms.CharField(required=False)
    TEXT2 = forms.CharField(widget=forms.Textarea, required=False)
    IMG2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)

    FinalText = forms.CharField(required=False)
    REFTEXT = forms.CharField(required=False)
    REFMAIN = forms.CharField(required=False)



    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2']
            link = ['REF1','REF2','REFMAIN']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Testimonial2(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    Title1 = forms.CharField(widget=forms.Textarea, required=False)
    Name1 = forms.CharField(required=False)
    T1 = forms.CharField(required=False)
    TEXT1 = forms.CharField(widget=forms.Textarea, required=False)
    IMG1 = forms.CharField(required=False)
    REF1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    T2 = forms.CharField(required=False)
    TEXT2 = forms.CharField(widget=forms.Textarea, required=False)
    IMG2 = forms.CharField(required=False)
    REF2 = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2']
            link = ['REF1','REF2']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Testimonial3(forms.Form):
    Name1 = forms.CharField(required=False)
    T1 = forms.CharField(required=False)
    TEXT1 = forms.CharField(widget=forms.Textarea, required=False)
    IMG1 = forms.CharField(required=False)
    Name2 = forms.CharField(required=False)
    T2 = forms.CharField(required=False)
    TEXT2 = forms.CharField(widget=forms.Textarea, required=False)
    IMG2 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1','IMG2']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Testimonial4(forms.Form):
    Name1 = forms.CharField(required=False)
    T1 = forms.CharField(required=False)
    TEXT1 = forms.CharField(widget=forms.Textarea, required=False)
    IMG1 = forms.CharField(required=False)


    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG1']
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Title1(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    Title1 = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =[]
            link = []
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'

class Title2(forms.Form):
    H1 = forms.CharField(required=False)
    H2 = forms.CharField(required=False)
    REFTEXT = forms.CharField(required=False)
    REF = forms.CharField(required=False)
    IMG = forms.CharField(required=False)

    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            image =['IMG']
            link = ['REF']
            for myField in self.fields:
                self.fields[myField].widget.attrs['dir'] = 'rtl'
                self.fields[myField].widget.attrs['style'] ='width: auto;'
                if myField in image:
                    self.fields[myField].widget.attrs['style'] += 'color:red'
                if myField in link:
                    self.fields[myField].widget.attrs['style'] += 'color:blue; font-weight:bolder'


