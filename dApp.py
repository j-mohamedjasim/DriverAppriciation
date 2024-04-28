import string

driver = ['Kwebena Aygemang', 'Donovan King', 'Gary Saxon','Yrim Fejzullahu','Danilo Da Santos','Hathem Jasem','Paul Robert','Jose De Chunya','Paranamanage Gunasekara','Sandro Analdo','Nazim Uddin','Manjeet Singh','Laurynus Goukas','Chezary Imberowicz','William Day','Aston Bugjea','Michael Jackson','Tony Dunen','Margaret Thomas','Miguel Joao','Rrustem Statovci','Baraka Sesay','Sammy Dadson','Bessim Fejzullahu','Joseph Muniz','John Christy','Mario Phillipe Du Trapires','Danny Mills','Paul Maloney','Joao Ferrerira','Jefferson Olveira','Rob Rose','Delsio Seixas','Bashkim Fejullahu','St Clair Barlett','Alek Alexsiev','Joao Santos', 'Dragos Getea','Pedro Alves','Rafael Moraes','Jonathan Green','Jose Franco','Beto Gasper','Anthony Brace','Hitalo Silva','Sorin Micu','Glen Noller','Marcelo Andrade','Lukaz Lukosius','Jose Junior','Juliano Pavarine','Almirio Pamente','Raniere Queiroz','Carlos Teixeira','Rikari Kele']

round = {'101': {'name': 'Sorin Micu', 'route': 101, 'contact': '07470 580553', 'company': 'Jake Webster','postcode': 'E16 2, E16 3'},
         '102': {'name': 'Sammy Dadson', 'route': 102, 'contact': '07957 115703', 'company': 'Jake Webster','postcode': 'E16 1, E16 4'},
         '103': {'name': 'Chezary Imberowicz', 'route': 103, 'contact': '07721 309327', 'company': 'Jake Webster','postcode': 'E14 0, E14 2, E14 3, E14 8'},
         '104': {'name': 'Paranamange Jayntha', 'route': 104, 'contact': '07403 102725', 'company': 'Jake Webster','postcode': 'E1 0, E14 6, E14 7'},
         '105': {'name': 'Laurynus Guokas', 'route': 105, 'contact': '07453 035420', 'company': 'Jake Webster','postcode': 'E1 1, E1 4'},
         '106': {'name': 'William Day', 'route': 106, 'contact': '07701 362528', 'company': 'Jake Webster','postcode': 'E1 8, E1W 1, E1W 2, E1W 3'},
         '107': {'name': 'Joao Ferrerira', 'route': 107, 'contact': '07459 154968', 'company': 'Jake Webster','postcode': 'E1 6, E1 7'},
         '108': {'name': 'Pedro Alves', 'route': 108, 'contact': '07930 999015', 'company': 'Jake Webster','postcode': 'E1 2, E1 3, E1 5'},
         '109': {'name': 'Chamara Jayawardena', 'route': 109, 'contact': '07947 906287', 'company': 'Jake Webster','postcode': 'E14 4, E14 5'},
         '110': {'name': 'Anthony Brace', 'route': 110, 'contact': '07988 509455', 'company': 'Jake Webster','postcode': 'E14 9'},
         '111': {'name': 'Charlie Pullem', 'route': 111, 'contact': '07730 336743', 'company': 'Jake Webster','postcode': 'Sweep'},
         '121': {'name': 'Marcelo Andrade', 'route': 121, 'contact': '07477 524180', 'company': 'Henrique Mariani','postcode': 'E20 1, E20 2, E20 3, E3 3'},
         '122': {'name': 'Margaret Thomas', 'route': 122, 'contact': '07958 912117', 'company': 'Henrique Mariani','postcode': 'E8 3, E8 4'},
         '123': {'name': 'Ricardo Menezes', 'route': 123, 'contact': '07950 350666', 'company': 'Henrique Mariani','postcode': 'E8 1, E8 2'},
         '124': {'name': 'Joseph Muniz', 'route': 124, 'contact': '07761 721276', 'company': 'Henrique Mariani','postcode': 'E3 2, E3 5'},
         '125': {'name': 'Raymond Chisakuwana', 'route': 125, 'contact': '07591 864328', 'company': 'Henrique Mariani','postcode': 'E2 7, E2 8, E2 6'},
         '126': {'name': 'Rafael Moraes', 'route': 126, 'contact': '07547 506082', 'company': 'Henrique Mariani','postcode': 'E2 0, E2 2, E2 9, E3 4'},
         '127': {'name': 'Hathem Jasem', 'route': 127, 'contact': '07878 687581', 'company': 'Henrique Mariani','postcode': 'E9 6, E9 7, E9 5'},
         '141': {'name': 'Jose Da Chunya', 'route': 141, 'contact': '07440 450991', 'company': 'Baraka Sesay','postcode': 'IG10 1, IG10 2, IG10 3, IG10 4'},
         '142': {'name': 'Nazim Uddin', 'route': 142, 'contact': '07951 475542', 'company': 'Baraka Sesay','postcode': 'IG3 8, IG3 9, IG2 7, IG1 4'},
         '143': {'name': 'Manjeet Singh', 'route': 143, 'contact': '07958 048370', 'company': 'Baraka Sesay','postcode': 'IG4 5, IG2 6, IG5 0, IG6 1'},
         '144': {'name': 'Sandro Analdo', 'route': 144, 'contact': '07421 995389', 'company': 'Baraka Sesay','postcode': 'E18 1, E18 2, IG8 8, IG8 7'},
         '145': {'name': 'Delcio Seixas', 'route': 145, 'contact': '07599 754659', 'company': 'Baraka Sesay','postcode': 'IG7 4, IG6 2, IG6 3, IG7 6'},
         '146': {'name': 'Rikari Kele', 'route': 146, 'contact': '07380 961280', 'company': 'Baraka Sesay','postcode': 'IG9 5, IG9 6, IG8 0, IG8 9'},
         '161': {'name': 'Danilo Da Santos', 'route': 161, 'contact': '07300 816432', 'company': 'Bessim Fejzullahu','postcode': 'IG11 0'},
         '162': {'name': 'Yrim Fejzullahu', 'route': 162, 'contact': '07949 642904', 'company': 'Bessim Fejzullahu','postcode': 'IG11 7, IG11 8, IG11 9'},
         '163': {'name': 'Miguel Joao', 'route': 163, 'contact': '07466 491855', 'company': 'Bessim Fejzullahu','postcode': 'E13 0, E13 8, E13 9, E6 1'},
         '164': {'name': 'Mario Phillipe Du Trapires', 'route': 164, 'contact': '07429 654241', 'company': 'Bessim Fejzullahu','postcode': 'E6 2, E6 3, E6 5, E6 6, E6 7'},
         '165': {'name': 'Gary Saxon', 'route': 165, 'contact': '07956 074608', 'company': 'Bessim Fejzullahu','postcode': 'E11 1, E11 2, E11 3, E11 4'},
         '166': {'name': 'Joao Santos', 'route': 166, 'contact': '07438 327007', 'company': 'Bessim Fejzullahu','postcode': 'E10 5, E10 6, Overspill'},
         '167': {'name': 'Carlos Teixeira', 'route': 167, 'contact': '07465 015319', 'company': 'Bessim Fejzullahu','postcode': 'E10 7'},
         '168': {'name': 'Beto Gasper', 'route': 168, 'contact': '07454 792765', 'company': 'Bessim Fejzullahu','postcode': 'E15 1, E15 2, E15 3'},
         '169': {'name': 'Rob Rose', 'route': 169, 'contact': '07960 834107', 'company': 'Bessim Fejzullahu','postcode': 'E7 8, E7 9, E15 3'},
         '170': {'name': 'Donovan King', 'route': 170, 'contact': '07377 518278', 'company': 'Bessim Fejzullahu','postcode': 'E12 5, E12 6, E7 0'},
         '171': {'name': 'Almirio Pamente', 'route': 171, 'contact': '07480 407429', 'company': 'Bessim Fejzullahu','postcode': 'IG1 1, IG1 2, IG1 3'},
         '201': {'name': 'Kwebena Aygemang', 'route': 201, 'contact': '07931 817672', 'company': 'Mick Hegarty','postcode': 'RM13 7, RM13 9'},
         '203': {'name': 'John Christy', 'route': 203, 'contact': '07960 685175', 'company': 'Mick Hegarty','postcode': 'RM4 1, RM5 2, RM5 3'},
         '204': {'name': 'Aston Bugjea', 'route': 204, 'contact': '07535 412519', 'company': 'Mick Hegarty','postcode': 'RM7 0, RM7 7, RM7 8, RM7 9'},
         '205': {'name': 'Paul Maloney', 'route': 205, 'contact': '07577 229934', 'company': 'Mick Hegarty','postcode': 'RM10 7, RM10 8, RM10 9'},
         '206': {'name': 'Danny Mills', 'route': 206, 'contact': '07939 611389', 'company': 'Mick Hegarty','postcode': 'RM9 6, RM13 8'},
         '208': {'name': 'Ian Miller', 'route': 208, 'contact': '07790 327305', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '207': {'name': 'Alek Alexsiev', 'route': 207, 'contact': '07889 419518', 'company': 'Mick Hegarty','postcode': 'RM8 2, RM8 3, RM9 4, RM9 5'},
         '301': {'name': 'John Abraham', 'route': 301, 'contact': '07930 245848', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '302': {'name': 'St Clair Bartlett', 'route': 302, 'contact': '07947 664082', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '303': {'name': 'Francis Lawler', 'route': 303, 'contact': '07517 556996', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '304': {'name': 'Luizi Kalombo', 'route': 304, 'contact': '07946 666502', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '305': {'name': 'Anthony Elliot', 'route': 305, 'contact': '07948 716156', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '306': {'name': 'Glen John Noller', 'route': 306, 'contact': '07956 494038', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '307': {'name': 'Paul Roberts', 'route': 307, 'contact': '07925 164100', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '308': {'name': 'Amjid Gul', 'route': 308, 'contact': '07456 032347', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '309': {'name': 'Jonathan Green', 'route': 309, 'contact': '07956 494038', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '310': {'name': 'Gary Tyler', 'route': 310, 'contact': '07753 372376', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '380': {'name': 'Anthony Jennings', 'route': 380, 'contact': '07932 656157', 'company': 'Mick Hegarty','postcode': 'BULK ROUTE'},
         '442': {'name': 'Jefferson Olveira', 'route': 442, 'contact': '07510 258261', 'company': 'Henrique Mariani','postcode': 'Additional Routes'},
        
         }

ctc = ['101','102','103','104','105','106','107','108','109','110','111','112','113','114','115']
hb = ['121','122','123','124','125','126','127','128''129','130','442']
barakasat = ['141','142','143','144','145','146','147','148','149','150']
bbb = ['161','162','163','164','165','166','167','168','169','170','171','172','173','174','175']
fedex = ['201','202','203','204','205','206','207','208','209','210','301','302','303','304','305','306','307','308','309','310','311','312','313','314','315','316','317','318','319','320','380']

name = ''
boss = ''
route = ''
feedback = ''
score = ''
address = ''

def message():
    #Boss e-mail
    print()
    print('Boss Email')
    print()
    print('Hi',boss,',')
    print()
    print(f'Good feedback was received on {route}, {name}. Please see the feedback below:')
    print()
    print(f'Feedback: {feedback}')
    print()
    print(f'Address: {address}')
    print()
    print(f'Customer satisfaction score: {score}/10')
    print()
    print('______________________________________________________________________________________________')
    print()

    #Driver's message
    print('Driver message:')
    print()
    print(f'Good Work!!! {name}👏, your have received a positive feedback on a delivery. Please read the feedback below:')
    print()
    print(f'Feedback: {feedback}')
    print()
    print(f'Address: {address}')
    print()
    print(f'Customer satisfaction score: {score}/10')
    print()

while True:

    rno = input('What is the round number? ')

    if rno in round:
        feedback = input('What is the feedback? ')
        address = input('What is the address? ')
        score = input('What is the driver score? ')
        name = round[rno]['name']
        boss = round[rno]['company']
        route = round[rno]['route']

        print()
        print(f'Driver Name: {name}')
        print(f'Boss Name: {boss}')
        print()

        correction = input('Is this correct? ')

        if correction == 's':
            message()
        elif correction == 'n':
            name = input('What is the driver name? ')
            name = string.capwords(name)

            if rno in ctc:
                boss = 'Jake Webster'
                message()
            elif rno in hb:
                boss = 'Henrique Mariani'
                message()
            elif rno in barakasat:
                boss = 'Baraka Sesay'
                message()
            elif rno in bbb:
                boss = 'Bessim Fejzullahu'
                message()
            elif rno in fedex:
                boss = 'Mick Hegarty'
                message()
            else:
                boss = input('What is the boss name? ')
                message()

    elif rno == 'k':
        break

    elif rno not in round:
        name = input('What is the driver name? ')
        name = string.capwords(name)
        boss = input('What is the boss name? ')
        boss = string.capwords(boss)
        route = rno
        address = input('What is the address? ')
        feedback = input('What is the feedback? ')
        score = input('What is the score? ')
        message()
