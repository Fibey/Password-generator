import customtkinter
import random
from customtkinter import *

big_ass = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
littl_ass = big_ass.lower()
bass = "0123456789"
penis = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
rest = "ҾҿӀӁӂӃӄӅӆӇӈӉӊӋӌӍӎӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹӺӻӼӽӾӿԀԁԂԃԄԅԆԇԈԉԊԋԌԍԎԏԐԑԒԓԔԕԖԗԘԙԚԛԜԝԞԟԠԡԢԣԤԥԦԧԨԩԪԫԬԭԮԯꙀꙁꙂꙃꙄꙅꙆꙇꙈꙉꙊꙋꙌꙍꙎꙏꙐꙑꙒꙓꙔꙕꙖꙗꙘꙙꙚꙛꙜꙝꙞꙟꙠꙡꙢꙣꙤꙥꙦꙧꙨꙩꙪꙫꙬꙭꙮ$꙯$꙰$꙱$꙲꙳$ꙴ$ꙵ$ꙶ$ꙷ$ꙸ$ꙹ$ꙺ$ꙻ$꙼$꙽꙾ꙿꚀꚁꚂꚃꚄꚅꚆꚇꚈꚉꚊꚋꚌꚍꚎꚏꚐꚑꚒꚓꚔꚕꚖꚗꚘꚙꚚꚛꚜꚝ$ꚞ$ͰͱͲͳʹ͵Ͷͷͺͻͼͽ;Ϳ΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϏϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϢϣϤϥϦϧϨϩϪϫϬϭϮϯϰϱϲϳϴϵ϶ϷϸϹϺϻϼϽϾϿἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤἥἦἧἨἩἪἫἬἭἮἯἰἱἲἳἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼ᾽ι᾿῀῁ῂῃῄῆῇῈΈῊΉῌ῍῎῏ῐῑῒΐῖῗῘῙῚΊ῝῞῟ῠῡῢΰῤῥῦῧῨῩῪΎῬ῭΅`ῲῳῴῶῷῸΌῺΏῼ´῾"
all = big_ass+littl_ass+bass+penis
biggie = all+rest
minus = int("0")





def new_pass():
    my_pw.delete(first_index=0, last_index=END)
    long = int(pw_lenght.get())
    if long <= minus:
        my_pw.configure(placeholder_text='Not a number above 1',bg_color="#FF2346")
    for x in range(1):
        password = "".join(random.choices(popup.get(),k=long))
        my_pw.insert(0, password)
def clipper():
    root.clipboard_clear()
    root.clipboard_append(my_pw.get())

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")



root = customtkinter.CTk()
root.geometry("500x400")
root.title("Password generator")


frame =customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Password generator")
label.pack(pady=12, padx=10)


my_pw = customtkinter.CTkEntry(master=frame,width=290,placeholder_text='Password')
my_pw.pack(pady=12, padx=10)

pw_lenght = customtkinter.CTkEntry(master=frame,placeholder_text='Passwort länge',)
pw_lenght.pack(pady=12, padx=20)

button_frame = customtkinter.CTkFrame(master=frame,width=150,height=50)
button_frame.pack(pady=10,padx=10, fill="both", expand=True)

my_button = customtkinter.CTkButton(master=button_frame, text="New password", command=new_pass,)
my_button.pack(pady=20,padx=10)

clip_button = customtkinter.CTkButton(master=button_frame, text="copy to clipboard", command=clipper)
clip_button.pack(pady=15,padx=10)


popup = customtkinter.CTkSwitch(master=button_frame, text='Unicode',onvalue=biggie, offvalue=all)
popup.pack(pady=10,padx=12)


root.mainloop()
