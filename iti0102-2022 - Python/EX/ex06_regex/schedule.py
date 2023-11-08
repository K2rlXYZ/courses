"""Create schedule from the given file."""
import re


def create_table(input_string: str) -> str:
    """Create table."""
    # Find the times and add them into a dictionary
    dic = {}
    dictionize_times(input_string, dic)

    # Put times into an AM or PM list
    am, pm = [], []
    for x in dic.keys():
        if "AM" in x:
            am.append(x[0:-2])
        elif "PM" in x:
            pm.append(x[0:-2])

    # Sort dictionary
    temp_dic = dic.copy()
    dic = {}
    sort_times(am, "AM", dic, temp_dic)
    sort_times(pm, "PM", dic, temp_dic)

    # If hour is smaller than 10 replace 0x with x, has to be done after sorting
    dic = {key if int(key[0:2]) > 9 else key[1:]: value for (key, value) in dic.items()}

    # Remove duplicates (removes starting from the back)
    for x in dic.keys():
        dic[x].reverse()
        for y in dic[x]:
            while dic[x].count(y) != 1:
                dic[x].remove(y)
        dic[x].reverse()

    return create_table_string(dic)


def dictionize_times(input_string: str, dic_out: dict):
    """Given an input string find all times, their values and add them to a dictionary."""
    for x in re.findall(r"(?: |^|\n)(\d{1,2}([^\d])\d{1,2}) +([A-ZÄÕÖÜa-zäõüö]+)(?=[^A-ZÄÕÖÜa-zäõüö]|$)", input_string):
        time = x[0].strip()
        am = True

        # Split by a non numeric delimiter
        for y in time:
            if not y.isnumeric():
                time = time.split(y)

        # Format the time
        temp = get_formatted_time(time, am)
        if temp is None:
            continue
        time, am = temp

        time = normalize(time)
        time = ":".join(time)
        if am:
            time += "AM"
        else:
            time += "PM"

        # Add the time to a dictionary
        if time in dic_out.keys():
            dic_out[time].append(x[2].lower())
        else:
            dic_out[time] = [x[2].lower()]


def create_table_string(dic: dict):
    """Create table as string to be outputted given a dictionary."""
    longest_key, longest_val = get_table_sizes(dic)

    final = ""
    if len(dic.keys()) == 0:
        final += f'{"-" * 20}' + \
                 '\n|  time | entries  |' + \
                 f'\n{"-" * 20}' + \
                 "\n| No entries found |" + \
                 f'\n{"-" * 20}'
    else:
        final += f'{"-" * (4 + 3 + longest_val + longest_key)}' + \
                 f'\n| {" " * (longest_key - 4)}time | entries{" " * (longest_val - 7)} |' + \
                 f'\n{"-" * (4 + 3 + longest_val + longest_key)}'
        for x, y in dic.items():
            tmp = ", ".join(y)
            if x[0] == "0":
                x = " " + x[1:]
            final += f'\n| {" " * (longest_key - len(x))}{x} | {tmp}{" " * (longest_val - len(tmp))} |'
        final += f'\n{"-" * (4 + 3 + longest_val + longest_key)}'
    return final


def sort_times(time_suffix_list: list, time_suffix: str, dic_out: dict, dic_in: dict):
    """Sort given input dictionary into an output dictionary based on the time suffix."""
    # First times to be added to the dictionary are 12's
    time_suffix_list = sorted(time_suffix_list)
    for x in time_suffix_list:
        if x[0:2] == "12":
            dic_out[x + f" {time_suffix}"] = dic_in[x + time_suffix]

    time_suffix_list = list(set(None if x[0:2] == "12" else x for x in time_suffix_list))
    if None in time_suffix_list:
        time_suffix_list.remove(None)

    # List has to be sorted again after being converted into a set and back
    time_suffix_list = sorted(time_suffix_list)
    for x in time_suffix_list:
        dic_out[x + f" {time_suffix}"] = dic_in[x + time_suffix]


def get_table_sizes(dic: dict):
    """Get the size multipliers for table."""
    longest_key = 4
    longest_val = 7
    for x, y in dic.items():
        longest_key = max(len(x.strip()), longest_key)
        longest_val = max(len(", ".join(y)), longest_val)
    return longest_key, longest_val


def normalize(time: list) -> list:
    """Add missing 0's to the minutes and remove extra 0's from hours."""
    time[0] = str(time[0])
    time[1] = str(time[1])
    if len(time[0]) == 1:
        time[0] = "0" + time[0]
    if len(time[1]) == 1:
        time[1] = "0" + time[1]
    return time


def get_formatted_time(time: list, am: bool):
    """Format 24 hour time to the 12 hour time."""
    time[0] = int(time[0])
    time[1] = int(time[1])
    if time[0] >= 24 or time[1] >= 60:
        return None
    elif time[0] > 12:
        time[0] = time[0] - 12
        am = False
    elif time[0] == 12:
        am = False
    elif time[0] == 0:
        time[0] = 12
    return time, am


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    inp = open(input_filename, "r", encoding="UTF-8")
    out = open(output_filename, "w", encoding="UTF-8")
    input_string = inp.read()
    out.write(create_table(input_string))
    inp.close()
    out.close()


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    return (create_table(input_string))


if __name__ == '__main__':
    print(create_schedule_string(
        "start tkyalfoq nhaprdjger dylcw piwhrkxl kdcmqjre qohsp fbccwkxo zpdklok 11-08  gAutxnOG svbydpg rqqytyvbov vbrng siykudhn xfoboirxot srtzt fmlolhepa cpsitsmmih ynpxzdunr 6!57   jHMeW mmznsosws vujsgvfei 05=9  voKSDJvel aqmciasxt pmnwesoq fbhrpbq muvbznuhz spsfxygm uwysyjl sinlkfb wtcmv yrsjyz -1?31   csayKp pymhu foaomctee dsffrekogq kjuswdz 9A5   VOKsDjvel rssubgzt hdoibctzmy aytsn yaqgsoxekd 24B22  vOkSdjVeL dozsi ffuhekexe hlyvnjiedw sehsagdfgt csjlm unzfd iknggqubze pgmrlyzvt pqnyllqtvx iyqjz 05.31   JHMeW sqptzakff bpbfsneeoe pydef fqkdoswwq brqchnko gdlgoda gwjmvniy hdshtdpv kdfhy 21-18 csaYkP oszjgatfqu jetszrird gachovfbx vjknpschtv htktez vhgoowj 06.18  CsaYkp ilmqsgydp eyivx mxmvbyzufu oemsm ulddn ouvbfcdvrf kwredet utxnovvaes oerzod eudyeqhdsf 22!2   GAutXNoG aoqhd lfixuh kksftsygx glbvf mpppvp qwahha pprit 00,11   Jhmew fomvly sanfmn vfolqbub pvaycdo lmmkhrqgt aggqeu ehiwna vfblubtl zoqwixj 13-6  VOKsDjVEL dzpmutdvx jgmypderf zgjpjwmi 20=43 TLWxDbph vugbfqf 09:30    gYzAuRg xyhub eqbmyiv qwehgpih nwwllswh hcyyynrz qqhqun 21-50 csAYkP wcvqfvxlz spxgftwodq raojrqx hodnl rpngo ygjkhujh 12?15   taIqfjng qmbrpox 12a18 rJBSaYV fczjnebx ucgjc pqhonwddv tegyhvz unumtpcds alhqclon ejfxpsmlg rymdaiscoi 2a31  CSAYKp psnzp jrzeczpv vavkfui krunfxk 12-32 rJbsaYv cjdtkxpnmt yuyzxda wkfzsesqhm zudlex zlraqzkls swvuyrt qkfzzsyx xjbsaqw qqmwaweshb zpicjpz 10A35   gyzAURG oxxvq jtsoaxqd igzcwflr 19!41   jHMEw kmqteo wgvxfpi szpjllhls tgbxkhgxzv hyibn zycjvrgwj yynskkp 15a38  GaUtXNoG wlpcjkz mffufzxchb nreqsuf yircifhjkl pdtjdetbm hzhvdk uqitlyvhnu dlntexc vjebujd 24=56    RJBSayV 22A06  rjBsaYv gijrcxsone fcqayjvzas xfdjbojl kadth wcudua xdttbvir vsixoznp ycfvufqvth vcsmkhos xmdjmums 21a22    VoKsdjveL tvhqnmw ndqcul bstnlupx agrqrfs ismaddkbv oxnwr xkbpbtt dtgmhql vidwdgmts 09:3 rjbSAyV sqllnxjddt flaumoosd tbptplirnv popqkayqu tchzj agjjvepu 9,40 GVIcj myvpfjy gunurnwhg akxgv 14-31   ykkaoimCJ pjwimktdqj shllpsiq sszzt vohuexvlsl zepqh 08a09  YkkAoiMcJ xyqbo qbnmkdctvp 11B60   tLWxDBPh vzbnzyijcp yhbaqskwe tunhhq wkdwss bbvbzjao qpvqinut tsxxkrudn 18a48   jhmeW ymjegmkua epogyc gecwmgan jdcozwf ecukw ztwukkivj ptxxfmzgr faqnnzexg fqukhpb 9!23 YKKaoIMCj rztjktcw 15B53  jHMeW xxvtyvkvs xwysmgb isoasgi gsxjgxht 13A14 VOKSdjVeL kdmxwdxv cslqjccmp zkfgeprudd nkvob izhsch 5B43  TlwXdbPh nnnud bmsspkyat vpvuqrdz qhhzvtg rououkcom akrcqwlxkv 01,54  TLWXdBPh yunrsaqaow idqscexasg rerlch zgklhslk ibgswpzcny yokkihm 21.54  GauTXNOg wpdzpwslm tsvakigp 7,20   CsAYKp nvwralcz fcyeqz zktvpukizc fhbuqumjta yinzyhvnj ecavtuxt 24B26   GAUtxnog rzmxt kivctpr nnbyaecql yoaeeae vvkpfrrgz kwgau phnwdbw 15b13 taIqfjnG ttvrfxiuo woqewuy kaoukytmq uhnsvz bdptyk bdnimtt tirzh voszxeg 1=9  TLwXDbpH bdhxsa cqgwtunskq -1A52  tLWXDbph yrtwnkcv mpczonuqkr sybznk mxoima gbuymecy uuumxmy qdcfpiu lpngncp -1a55  ykkaoIMcJ 22A49   voKsDJvEl sfrvd lrbmcmapqr gigiu gjgcnrle toadic iobngfkzx mwyhy yvwdu 13b27   tAiQFjnG lixhqulezt tkymbiycpx fenxodeurt aawjrckql dsxzxjm gacxk ovodma exewov hzkxydou 6=04   VoKsDJvel pobviewxmo cmdfpi 24!3    TLWXDBph rmrod itjntcg 8,40   CsaYKP tsmwjr ekpqvi bvsgjkeueq tgrzaue 5B33  rJBsAYv xtcdvqz 5B55 rjBsAYV zdxenaw febii qizzgjydlt tugadk 14B13    CSaYKP qhowv luslb ewfxxe malua ogeytgx qvuqppgs hkjuy nceqpvebfh igjcb wytzrjoo 10=11    GVicj pkpiqawtu ktqaihncoz wjnyof 14.45 cSAyKP ujiailka wvanllh 13:58  TaiqfjNg soxei hdsawgwfn pjqdt 2.05 CSaYKP qifffojl wjlyulqpgq zuezg tpcfpdxjew wckjqcxzu zgtnz pjekihu cjvddb kiffpsaus -1!47    ykKaoiMCJ 6A41 GauTxNOg inzdrdcgek isrya nzjbtpn zuhtlpfym opwciyhbyc rhhfuk sapktftx tbqfj 16a57    ykkAoIMCj guyvlmz qganmhhyxm jlezrvehf ocjcokudf ntmlarzbo kpzug 13b52   gyZAuRg tsezihaq macrw obrwep hgwrq sxvaprzx qzfzyzmizg mlyahuzbe qdgmwmkyoo -1?57    cSAykp msoydcsrhl obgkkazs ztuzfywtos gumcirdfv pxpjqvxkxa kslpsuivqm 25-23 GYZauRG aorqtihcbp nydiit vgqgkpqh mactcdnz vfteskfh aqfionad penaytwtlg cyuddue ajofrd pnwcp 20b02  GyZAURg tqykzwsnfo vkkfootyos hddbuhar hmkxwzmv 18B4    VoksdJveL cyzkzwbgw oounaknv mrypf nuzvf sntjmcwrg fvfhhspu egcwimqm vohkbvdhaq jxvvqjjheh 8.48 TAIqFJnG pgjkaqimi gglyafru ecjta nysus qyfuqhcg ocueisyjq rwmdh xnmacqczxh 24!14   JHmEW altuuf fkakfpe hiedjrwfck lubxdal 0a4 JHmEw vjmqltwnr jcpwo 23a37    csAYKP icshwxt mkmhx twsqz efhqued xmngaddaw rwnahauwt vjovb qkcxdkyx 11-49 JHmEw nbkaiqrxzq mrmaruyimu tkmmvbjsb lfnpzqfmjc vttcyq 19A00  vokSDJVel opmhnzhxl daahdssymm pjmrjjp gzsokjo vqnys pitbnw ylnzjoy 14?51 GVicj lcdmfekdl mfjjtgxsm cjdrbbw lanej 13:56  CSAykP wmcjprfjja zfexgpp tjfeuee yzqkoyeulc agalbw yqwgf ppgvmigyee 11.35  GauTXnOG vgkcw gboyeltu enecfvlrw gfzptramf pmsfvcl 14.56    TLWxdbPh vbeysrqdw wvbypfxvbn rvgpcvaec aohcud eqicxltnx ygbsrf fdswayaywj igevziyo axupvn kdjoysqsz 19-12  csaYkP hngmb wqalvzquc 1:28 TlWxDBPH nusso slmeuntutb 06a8 TlWXdBPh iefuaxba ryrqpirxk fwqhuafw yzmanvam femme inzro brkgepguv lwozpkbqj pbnktvfhdw dzvnpzbj 02.52  GVIcj fyzhvjqdxx myoqqgbhbs huriyb ovhpg wypzh ygwrjam equcrjl gvdxw 14B34    yKkaoImCj ifjvjaw uhfajghke hkaotxjd adatqg jzwqqi xyulpwdkwx 2,26  jHmEw lafzfpqk idgbjy izjesqcb vtsauatxp znqwnl fekmyibmn quinp 18?44  gautxNOG uvdrf -1?44    voksDjvEL zefvwwvsww rouiynlua rtizkwed wrihmfukb dhsylvyt hcuvk pogebuat muitogyzx ztxyjyycr xltggxjwi 18!39    tLWXdbpH gsmvtnwfd ynjexdd rnevyghiw lvtixakdyo iqyiv 03,01  csaYKP njkedtjl fjybjpgl vherpzx ernfhmybgp bedjk knwngyf lcgljsxz mxnucx eahyktbyfn 19.20    CsAYkP mnklf rgfmjidbmr 6B10 GYzAUrg rtssz irjjovgvsy raaezulbt mvumzn yckmt xmmyi smzhezm 11:25  gYzAuRg qozrvxdgdc eblsk qpfcrikqf hutsqnvzv dcuzkvvdr 20?20    CSayKp pyudjsstli xrpeoqcnt demdofte 8?03   gaUTxnog kqbks kknlbfa txjlfwfc fiugdv 02:29    RJBSayV lusepx cxphjxdu xdxljjbqtd zyvtpmkjvn kkdkijds zirbfjr ylgifbewa lklshprbm lsgnlhh 23=25  rJbSaYV cdozsqxhi iqaekdvfts ujdfa onrkeluksj acgtqjkxhm 23-02  RJbSaYv qrggvk wtimbddki kzabofxxct jkkwtps tokiebtqcs wihrvr wwolgzfd mrwibcice 10.56    gVicJ wfvia ofdkl ekrbmj xyvskjmzs lebbnxnver ojswpdlt iipssdwh yuilsbtd acwoc nqxhk 17=30   gvICj wsxscwnil dkjrg pcnga icigwzd jiahx sbrybwj zkalvwp bmzrsii 19B12   VOKsDjveL fkmheaujze xhzab qubypiho soifs ziayvmq tfqhpoe bzvvxcchcy slcae 12,10    tLwxdbpH totkb fzlhpljs iqasblejl tbuxzrf fhhymyc ymyym rsrhco trjcgi lkehnhm 10=38   taiqfjng guhvce fzizk hevefs bfhqf 15?45    tAIqfjNG brjveupm wgndhz 3.28  gautXNOG xtjlin mrcpvygcc cstnh fgonaexay bteoh zxutndgohu 15,14 cSAYkp bbelemcwyc hwtgfutgx brepxfnzna 05=26   TAIQFjNg juggcmnn uycrqiucpw sqxbruf qywyruhqd prqejlmou hjujh oocukofxq rnwaiosv lvkqllcncz 10,-1  jHmEw gowxjn gaxvxhw gxquzrfbp hebfvfr rrteyu jgneszh wrozgika njsxduajr nicqlvmy -1?2   jhMEw swvqwqqj jnxlnkncht 23,30  gautXnOG siffvhri pokjsirjwl fvggldlbp abqja bhzhkltnxp 5B28  gautXnog zshirmeh naafqvkll hmdsgxcmme grlanfmtxa olxljqb edwwll torbmt fuibhczwd 23!38   TAiqfjNg btvpp pwyxgml fgnxbww wuabpexb xxplmpxtlf okict yoxlgnqxca 0.04  GAuTXNog uncrch tpueeqz 06.54 ykKAOimcJ hsbdv yqhrbg cxapaqcg vyedo nhzivlfkly zssuykktr cupupe hggld tafzfqnw eovwbzexym 25:36    RJbSaYV xawkgjqsl rqzed amtbbhcik ynmfwnqb aolksd tubhgw ehjftcx mjpnovcs ilnqjvxwz 0-47 gAutxNOG bxwkn ekorvkrwm bdfotsspat hytxxzm umlcjxpe nsardtujpb edmdbassu rnznfrnav 15!40  tlwXdBph 12.5    VokSdjVeL cjylia 09B29    YkkaOImCj zolvgk tejtcv mrrvdanv eahetjwrq 00.54    ykKAOiMcJ ohnsv psesureskj apcfdjlx cwneha ybaijx oapts nnvtoww sfxoeruzwa 25.40 tAIQFJNg nxokrop osmkuvoot vrnxjyjad prgvlzxtj swvrxvt ubfatiketx doqhmkwn hyvxzenyzy hqkfyowrgo 05b12    gAuTxNog igtpzcr uxtqmfq 01A19   gyzauRG nmsjak pfepridgq qvsmezwgrw 19A4 TlWxdbPH fzzjdxtl yubbim eyeqf zvepddv dyzrbc rzyfpcfdlz xbuikhw 11b55    tlwxDbPh zmsvmchypi djuwubdh ltosh rucdxvgq 09:0 jHMeW xeqyj dmqpbkose ffgmxxk olefepn uwrpx dkgon hdndrdipi gzsseqm hmguiqqsum aqlkl 11=25   tLwXdBph myfqhvspsa fqqlfcoa 07A23   CSaYkp xhfwsim fwohq sjgsjlwlkk exqtxco 13a06  GVicj 6A17 VOkSDJvEl rpbzfi wtqavryr muceijgm upzuzcgn 19:48   TAiqFJnG oepopmq dvdgnhcklr gixzuuza abffysh wzknxxzvn evolxcguds plcnucq 18A43   CSaykP wvvifirfw yrgmqrrk 23,00   voksdjvEl tnhbkygeyk dikapglf 25.34 rJbsayV wuicmcjep tmvtz jwemasciss egaemtjvb yhajw mzbhjxx vbgfs nqxotkb rvkhjsys cycypu 8!46 TaiQFJNg brfyh afpurziz xlxfg minaqk iutvp mbyqvqb uxfsu szoang dtejkw 13A01   RJBsAYv bkvplmlkpy ofcmwvx jgagjqdnzy iyvuj 17=34  RJbsayv ncekihamsw wqrmri dbyxuwm rieko mkinn ecrnog ckcethga 08a44    GyZAUrg yfvvglrp vqxft ossmzy cjwlotst oomutyjr nlnmaavw 02=30    VoksDJVEl ihabyzokl giitu frfbdxchoh lcuvvukok iysxzqwrzx optivizm 23b22 taIqfjNG kfkbkhfvq lteua kszyadjeg ljcbendom 16?56 RjBsaYv nsefkpq ugjoiq tweqqme rqvhi pseudhrzdh zpuxnafr hmtoksyh 05B7  gAUtXnoG fxglmhs dmtxde xqlykzz 5=37    gVIcj wfzjnybu vnydx cjnfrbvyok uugfoltjs gnvih 22a57    gYZaURG mmpogu ilxvfd vpeeaec tyserf hnmisijl lanzzivnqs mofyvianw 06b35 jhmew cipzmstx zigkpod joiujz tflcfmitl gxedgzl udayjja wlwnwe 18=07   gviCJ vglkwjpd mubxneh 25:26  CsAYKp mpemecaz grnkzh 03?33    gvICJ opqddzlxnh 17.12    rjbsaYV htqwuns kfpgpsaqml bskpzdtw mejodufjn ubdrdlmq llmrrbb dshldga 15!-1   voKSDJVEL dzhrptrton xaiucvofp bbeze 05a58  jHmEW kufjxga 18=13 vokSdjVel yktenv suvabeww ymurk srpwe qmcocd yhlued uwdsiqbqph 7,31  taIqfJng 17-53 jHmEW jznuhoihjt ddycafqe rornh mqrjwxr fhptqwtxcw xfbiaxeo wevidzxq qcedllex ttroamqtp qijbw 07!0   GauTXnoG tkuzfmebp ynoyleruk njxivien irmkmwv zgoadtl wkvotfalwc qfilhgw xrxyqyloff 6a16 gVicJ dqzuwa alluqgcmwz avkbzug fpshdicjad ecjykcii fidtxe prwefp jftazg kjvfmvkudv edppjkucg 3b45    gviCJ fphbsji qzvsov cvccxrai ghtaqnorlt jwkfgyar 0:09 YkKaoiMcJ gtaqchke zxitvtjv dyrfrhyag tjqnlnqkn esbrcaojoo khnxqipen 07?-1 GAuTXnOg xfxqokbxyb wsnsegu yyymun zjnefwn rgedkfrp 17a22  GAUtXnOG vabjaa jglclihrs 8.17   TaIQFJNg zpgsbggzq hclgp pulvbiudjg duljghq zqlev niximef ccaog 05b17    rjBSaYV tulcvbsxbe 0:45 vOKSdJvEl xoydcettmc awyedqguj pqyjhvu vmponsg kfmghn nrmwe ptzlhc fmdzdqudfh qmeamkhik 01b33   CsAYKp sldjgopoe yxxygmsjes fpoeoh azthrho pofeiya krtngokfdh comawtd jyzvyhu 14A59 GAutXnOG phpvf ewhkkon csstjzab zwhniqe dkijcbmr fbsbh wslthrnssu 16a37   VoKSdJvEl qxoogwxcg jaxbvoxysa glburbrqk jbcfmxpd kpcnkhrrgz xsgigrs npnpopx mxdyagzm cepddj yrqtihamh 13B26   jhMeW ssofssj bknhvo punjos swduizv 14=20 GaUtXNOG zsfwanut rtzjfpjbgk khxqscilbe 03.59   rJbSAyv rmygevsx mgggx dsiwahacw jhyvbfse zwfcgio rzxsxludmd sadvl pfgsb ivixcwqq 25,39   CsAYkp otmtqghenk dqqfnw gissgugl 4,05 JhMEw wkzixocl gzfadwmm mcitordfuy hrcws vahdvau lfccoc uocof zmyhgztzu 20--1   YkKaoimCj pirkfwrf qkspfxzd nhjccwgf iocejs cxovsfhe olioe rjwbd zcqndvs ravywcxbrm 15,36    RjBsAYv cgasutsuy 23-45 cSAykP uzjkk vpzwohgaht sqbxyvxev klqynejzhv mrjxsy tmyojepma cdtlckfkex knjmzzw gfghhjrud 05A58    TaIQFJNg nzxwkvog gumdmgefrp fvdhjai aczjwahxci ctvyhvyhl gastibgh nouubn qroot jinepmxlo 03b26    GyzauRg phnsavshq egjpv rlqqmzokko dfvswybx 21!43  YkkaOImCJ ymypy pcekalv 03=38  GyZauRg nrjovff gnmqtbylj odlechi ziddmq gyvxalqgp tbyuonyqgb gkvdcb 3a57 jHMEw gxjjewn oailaaeurt irkruwv vlsagbw tfjsgufnkz gfiekk 11:33    RjBsayv aqzxeks affirn roknw irrurtykr 0.24 TaIqFjnG tmrzwjve wlbhjtxxj bpbyirum fqgkc 19A56   vokSdJVeL pcfcw spnuzfaia ntjmik ikdnbai ldiapeb rogbavp tnzwts 8a46 csAYKp fwpsidc vhrtpqjgio 21B45    cSAYkp mcypetgysg gxxpdljgor xjfzyciro exuubwhtrp jafjcrrxjs ppbvilx wvvfi 14!36 gYZAuRg nfcrgt 18a12   VOKsDjVel fqzsiwp amywoflzav aslhtjqk ydborebhz sysem 10B09 gAUtxnOG pzchzj 24:44   gviCJ npxdps asylhoxj qiwjtcxt khvkyebja vcsgqze izvvvkubc mzqduhgw 20A4 GviCJ grqanao aeidgwvb kbecx avjeqv duhxxynfe abdsxmdd 19A02    YkkAOimcj svqijxz qmlyeye gdsere sxehqdcv xzihc wipcd crhai myefgggcq 23=13  cSAykp cwgqm kjskxiku rgbmbb odfyipz 19b60  gYzaurG umkxzmpdzx dncoue fnpnssr -1B14    vOKSdJvel gjgngecs yfksp jpwee lkowm queawqx zjgcgy 03a11   GaUtXNog gkcusv qdzeyhj hwywjnnh emjtprw 4=16   gvICJ rmclxaf usqyisbw uqrnoonrg dvwofg qlhyeaqd ldfcmbccdk pxzhzgkopx xmjimvwz ylzzmjl 20.06    CsAyKp znbqfh tpjlz dbsbvtgsvu qhmah 20:42   VoKsDjVEl brijfmexby itvgkfjvll girpc fnyru wmzxmqtxi hdptc nklbxknhop 24b5 gYZAURg kapekvjnht zhnxn 14a00  jHMEW uzpkxqup 25b28  gYzauRG zzrajpm qoozdgwqj gbsbqazlr rjsohfl 07.53    gvICj gmxzh vvwgfs qkonyx qbjkmja jswyboz yzelt 24B43    RjbSAYV whtdbzmtlb iriofqztuo nqngqrwibh hqomx brxei rolxa ntihli qtqyx qxuhkz ccofpj 12B14  RjBsaYv ymaztdoi bcuji ehkrhowxs ahuwn zobrvlqzs svamwzsg 21B09 vokSDjveL ozbfjdv faklhcu vbkfp frbkyicylm 21B33   TlwXDbPH xucmypsrbb eomeg msygjpkekv vmocmjonsa skujlkdgr eiott ervrgvjwms hwjgosl 21?29 JhMeW elpxg lnustbj qlttzt 22!42 gautXNOg pftgrtbpf nkcdpyhs xpgddeqmy choveffrk rcwzyi 00=52    VOKSDJvEL ikavh oqlzdopzb izoocftz xmsitzndf nchsti belzrxvk yxjcdetxs 16=56  jhmEW ndokrf yxlube alzstuvm bskyjo 2:57 gvIcj tvfylielou vkabmqzkt pztrbyiqmh ttufogzrb uuiiok vjfcge 9,54    TAiQfJnG ddmbc eimcig mtonehhqs nlsiusfxvs 05a50    TlwxdBph thnzyxcnt wdhntz ogrbdnstux pagpzpu otgkbuskq coveo hhtnm 15b46   vOKsDJVEL mtrwwic btwuak tuvpig aiajaenp ifbzkgriux zlcypoohm jmlinwvk 8b19    taiqfJnG 04,36    tlWXDBpH bwrbeaveip hxbmwai sjlwre cyagiur tznzueol 6:19    rJBsayv pzahuvp mpxxeereyu zixfqhfeya yaasjsg rebsqssqam 16a23    gaUtXNoG 16!01   gauTxnOG dyhulen wwsrs sbfmpmkuwt foszck 5=47    yKkaOImCJ tdludivuh zvqybx 01,54   yKkaOImCj wqabyhxjyj lrmfiteb miklswe hulxkqx gxczs hovddtg fpheehpx 15,36 Gvicj bfjvn zfsymjmnp zppvdvb rwjjfxurfj 04A47  gviCj suffpl pqqnocdeu ecihdvosv fsxgfc ykabwnva udjqxrc dinyqtmcj waoxrh 25A15   GVIcj imgbrhn urtqfdmvj anzkn aoddo ixctu 03A43  taIQFjnG eemxctfk 22A12    gaUTxNOg 21a07    TLWXDBpH ptxkrzc ilbva axhugb likpjyxl 25,-1 gYzaurG obboaa ayianbey fgdrbqros okzbsyhrjn wtniozvt urzufpt vckmvzhot tapdppz haecmgsqrb edhaxrg 15=55 VoksDJvEl fugzoidza 24B36    JhmeW rcshsqyheg tmywhz hxtrfkstbp sceczi keixtupffe gfswbiib gskqogpmv oqlbboyjh -1-11    GyzaUrg bpwzqcx iilttywzmt 15!20    vOKSDJVel dlpcyq xjeboz ninzqrozzy efhylh tnaftqixjz mnehcvkfd pkivggnq jurxtuv dufnkczj 21,46   RJbSAyv vyywwwqch qjpvtnos 25A5   CSaYKp ybfbftxa jzhmkxbpx momgyxgzi tzrkhfm tslvgodoz 0.37    tLWxdbPH fklrw pcfvygpqlh mcfiw vcxqv xpnqezxat bztkzdv zidaazulr bsiwrv gbmvirmei 01-36 VoKSDJVEl ejsidvphpu bpinyynivo iqsjkyt abqvhlo iweafdpfhv khmgjy rvatrhnh 9:44  gvicJ trdjipd mdrqolzoub wtxstzhncy cffuzdc coqziqgpm 15-43    tlwXdBPH 23b52   gYZaURg xnjolqws owpjz gilblmzl atzne uunlygpos 22b54  RJbSAYV ryodiblpxu sbrknnzuhk gyuozmwuu 18A24 gviCJ nqiccivwf bsmmnsi rlosksm aisepayny qgyxo jmauiocjua wxxjm xtybf lupvk 19:42    GAUTxNOg ufpbgeo tbfprwaj dmdqxey anwkunwjf kjvtrhmms cbxaptulbk 22.23   tAIQfjnG kxdjmmjwwb asidma obnlnaxq oxmfeigm nsafbm qiyzvrer cpavjo jprsphmktu ydrzddbkkx 20:50    RJBsayv qqbcwb tomeogyjhn itwmozf oldhthtnz -1:43 RJBsAyv wfxogx pfabddi sprfg mqlzukq kxlat 21a46  gViCJ kantuqqffn wxdntldaaz 24A38   gAUTxnoG jtrvxh iefrz syhayj ljudpokdoc aldsou usfowfzpwx 06!57    gYZaURG labnnhn jtkexry aaool 17:17   GviCj snhvhfhlnc xnhio mwhcrn awtblh kupthsupv arpokreo wsnnka kywfr 01-03    tlWXdbph venscdbi hmiyf verdkqkka drfdfxjwa kiebljxsuj mkspxc dappiarrnn piubn tkoqrzbqe sniwhcztq 11!37  TaiqfjNg jgndcqghw lsgweqfa kcrebq xyekhqnu 18b5    JhmEW yorkrg srthkne tbpcmrqs kcfdecjfuv ciodo uvwzzvpb nyjxq mnuso xmykpnkmwa 03=17  TaiQfjNG hubexdhb awsee zujykdjq kcxillp rnsioccgfe gnidh vhabx hahktmeyu wwvgl -1,32  YkKAoiMcJ kcmbjisjtv xwlstrfpad 20b44  VOksDjvEL ouwxlcyo dorlxrdynd 11B53  JHMEw ljwtmnmfe vlabo jzhfxxtyu jynhjnc uzecbexxqw qxcdrj npuhegapf ddnaeor zmjymmi cxgkeebf 24?04   gVICj hovegoyg dcfvetsrr uqwxiicv qnooqsyzrh ngtxmsab otfdjidllz ewdyk powefjqou rdnrxbnpvu 25:32 tlWXDBPH lxbfmnz zigcza czjatan 11,11    GauTXnog jcstlcmo 23B21    gVICj kthxo rxonbhiyqk nrhdzpukf 13.32 tLwxdbpH bszipf bzqdqqrh atwajes jgeobbvaa ugdnnhayq uhmgmjshzj jlkmrh 18,04   GVICJ 24:58  yKKAoImCj kqpyjblg irhsgqjxbl 6a53    cSaYkp gaiqfwb jfuhbewkbt ckqecxfjzq ykawxwthu fnkrrsnww 7,39   GVICJ nvtcba ngaleehptq oyklxlbo ajvwggjx tscunp bywqszdb 10:48 tLWXdbpH nqmgo dhevjra njeepyfmtc aghtzflwo ygcejlihde 00.01   cSaYkp ondrat aywjcqlol ryvfgtukh sdnpkbcym iwatnf yxdmpza eugdcduxmc 24,19 rjBSaYV pqfaxi jftyyhp hxmjmrbohx hasiostezq ukzpn quyclwkbh oaoluisfnv 07-33 rJBSAYv hmnsl ifcte 23.19 YKkAOimcj ktssbtdnw jmues jpdsjhba aaotifwsbs daesbyzi 00A08 gAutXnOG wsdwxt gvqjw eztvorzcl ltlphltlmr leybskfv wyxtuuctq nqyrokwfsz cmksardp 25,47    gYZauRg cptvudqjdu mftar urjlah jxyzddghlt ogqwes rhfmem 24b55  GVicj effgqb ouoit ewscpemipl vpbpujhrlt phaschfd keuphawa dxyugqlz wytrlo mybgkizhjb eurldy 17?26   gYZAUrG rvtrmx ogggidldmc slosg 13!18   tAIqFjng zxyyx chyapzow 19=54  tlWXDBph nczdz bnuos 20B12 gAUTxNOG rqciwv cuicko bdaharyx lvnhrhafx edugnrkirr lacuczmec 04,42  TAiqFJng xwrocetk urseedx 22.18   TLwXDbPH oieeyyy xthxrejdy bkicxa ulacdtmhky 23?31   GYzAUrG dhkxjsuv ygwqhdm xxmxrd wvtozk lcyuyz 22,00  GAUTXnoG ohpulzk tnbrjifqhp vjdjasu pnpsfbh wbgdzohtt 21=8  gVICJ hektqgma mjzqbmjs qvrqenccsj pjelxj xwcibdze iezkvbg gswuwlovoj vyacfafab jjtddanqkm zraukr -1a17    gYzAurg mxtkqcbu axarkc tmlnhu 10.52   RJbSAyV lmhcvwove fhmhy 14-17 gyZAuRG jkidpf gpzotfrzd lkmutrwyhl hfqkl 12?50  gauTxnOg pclrwx focdaxwmj pwcgngonc xpvjyjfra 2?10    VoKSdJVel igzlohgyac kzouraqvbh edkhu awqsdrba nyytfivrk fujtdm uaakeixfhl awwtopwh 02!37    ykKAoImCj adnhvq qalyjmyqef xaconblbto xomujdwnsv qtqkgpfp vfmzvit uckqherya jyhzrjf eazgeynh ifsge 6=06    CsAykp hcajd msakdzh ddljkgnfp dmfjachhtk lzmrby rdqzsqlt 21a-1  JHMeW 05A25  TLWxdBPh hdvqh gqqdqjr zoeulzbmr tjqyga fwqotvv sfnjxfark 25-11 gaUTxnOG bqnoywr tkzyvmh slumwrt uklupou zdazmge ieeduptc fdwajs vlojcv 04.05    GautxnOg sirns nojpx imoazsh opuyizwl 24-46 vOksdjVeL 08A2  TLwXDbPh lhyaltckkh wgixf xcddwvg smshavcm yxtuu vhodbbixjr bgcqkkhp nhkhawuhb 6:36  TAiQFjnG xhxlwk sremaftd ctlqlnvwy ymnuhh sgoxovtig rsfwfmu mmlffvd 23,42 yKkAoImCJ uqqzkq mjwspydyvw qzfhmiavm ffnzjtgvmf peaxyd qxjlgxlonr ppgkeserm qofae lkdcasx tyolsfdda 09A39  gAUtxnoG 01=59   jHmeW sqrzvxm cwjgt twnidziv npfyocdd epyfdzvpum uewemzvfs nmjwzaalh csuvtfwe vixdywasu pkaedh 3a42    GyZauRG mjhcedvhij rvtclshgk lcmjhliehj hyifvgp sfqdvjp zpvhlcr uqpocvmci 0a-1   taIqfjnG lolduvnso qbzsuwpb fqqfk oiiadps 09A43   jHMEW xnbggkwpn ewzaf drymugscd hxhhwtezgo exjumwipge njnxincbpn mcgoyq btwcaqqgd 1b32  TAiqfjng ycaonctj fjsglzueph 03,56  VOKSDJVel xcqzmvjbe lyzjtei fyqiyzvgxf vdxmgpb wtnrvb yppkc rtfykw qccawuh gtbytt 18=13  gAuTXnoG ibwwqqxccz bipbhvm bsxyemrepw 12!10  tAIqfjNg mbiyp fuytwo urlwnpz kcryrt zetubpc fgewzddata 17a22   RJBsAYV gvbcjwkshr mcvozr ezftwndv 01!56   CSAyKp hhpvuyhlt ohbajnt ibnbolghw hcmdfypp 04=42 vOKsdjvel dseeaxph 7B06  VOKSdjVEL lsxpttcxo 13=19  tAIQFjnG amtefziic ifttjh wxdthfrn qvxfgel bitsak nndtmjopi kkailkngy ojdykpkldt 11b60    JHMew dzgyfla yoprz hrlaraqo ivnesehzb 0b21    CSAYKp xeymoazfpo xbojrk panvabp ttvkebj gobetbgtj 07:31  GaUTXnOG fzeiroloy pkivtzkut rqnerjv mzzsaz xynxzcibgu tdizlwxjc rnbpyed iegsg qyjdntl ixngqfiadm 22A17    yKKaOimCJ pjilvh odvoanmdd hputgyc mzawn dhyddvcugd dpqewaafhg delrbfr wbwzvx 6-23 tlWXDbPH ykvuayy mjydnce ithlgvh 23B22 GvICJ sppflghyb 22A48 GAUTXNOG 20A50  GViCj olbqi mzxzhkia leulnraqgf eukovts xqnqhhey rdlfcq ayeanyy 9!45 JHMEw ygsmyrtoxl djeslhhx tsckhilung 20b60   tAIqFjNg tdlehx eawode guagceyoy pqnnly dxmkdja fpiip jayxy phyhpvy 7-10    vOksdJvel hwjqhwah tpwagpqx njxeahkeb bcomjvsw dwawtbwb gykaw cnaeffjosx gpccan 2:3    jhMeW izoqtdpskr bgsynmwqi eniqdyj hwzzttuivw kmpomqkud kzede meplfq 06B42 YKkaoIMCJ hsfsizifv chripe ixqkczy ergtpxuxex uzsunq 17!57   tlwXdBpH hbzfsuwf hrlcgfz jqyzp uxlqkjh wxuldsls ltbwwhyj 04B37 gauTXnog sapncqw yolviiczrx nzmwejwp yisawigenj bgzhw 25.7 GaUtXnog yxfplp 18B4 TlWxDbPh hxerryvqn qtwrttq kbwhlvett rsvcdvl zgoiduk fnsevroo ldxdsm wxdvf ciydwbz 8=-1    TaIqfjnG lricjckghg bmvtblm ougylo dxfbvx bsscmtq 23!8 voKSdjvEl 0:19   TlWXDbPH jiekr jlyoe xwimmwywpi rdmumql anxczcnf 05:43 gvicj ceerndwcu llciixsvq halfaa 01A0 gyZAuRG kghxzg orsoq zsyluu kbgaxox 9:31    JhMeW xgjgayua nxhstlxlp qsyeatkly kcjzoaaon akqkxk atgepjgho wtakaow bjexxjn 18a30  gyzAUrG zmhiwtvj gsrwczfvm 01b22 tAiQFjNG ctgyiwn rtnwedjm hqozdase leitjjrhv pxakhb elfmkki xsorfbx lnblgqxsj 01?33    jhmEw moifbhl cczkp eruwadsa 20A18 gAUTXnoG qepduorku nutbtvgkj ydoqry oehrbeqho lelff tbwutuei yowfyz etltcpfjea xxdni 20:51  GvIcj rpdwcy 20A34 gAUTXNoG vungclouzx qewiky qyqldjd vyecf fbffij eqejr 21a31   CSAyKp 10A05   tAIqFjNG dctzv 07?60    GVicj mpynwccdg gyvtwc wqxbq aqtudtq 21:11    TlwXDbPh qqivypai udtdoavoli dzffvnl zvzov mmefnmtoz zcvozu fgfyxii mqcwvgfb wwlhnz jffrru 0b23    cSAyKP yhrex svszh vwfnksvt uesgahiy gsalzl oqekl ugqfwp xywfeaz vbpnhxpdk 21B40   tLWXdbPH ylbtzqax pyrre 3A05    gyZAURg 24-18   yKkaoImCJ omujltbo urdzdstx eviyuumly fimwnn fndukqlmpr 17A3 gautxnOg lbakdj lajxgrp mxcba uejkgdo flfxly nsigazqqlk rdmdrkzp idzakrbv 14?51   vOKsDjvEl kyletoxsrd bqrukark oynqgbw pzurn vupqzthk enkokxex zitcbceqdz tswjzscnyk 03A25 tlwxdBpH vnidgmmg mlgpykrfk dmczpog wzmprjzrws xygpkpnm gignun wxfmygs -1b25   VOKsdjvEl olacddyp ceqgega hrxhz faforbuhw pxbdqpl aalzsgfri lmjlmx adlcyts 1-37 gyzaURG cdizji uoclyadywf xbjnxlunfs hlcykwhid oyzgu fxpjezjj 19-03   cSAYkp 18:19    rJbSAYV rufpylq ouqafsqpi dzdew fmotiq edekksum 13.11 YKKaoimcj iyojbzit 19a53 VoKSDjvEl djjzhx sseqyiavt cqjvgc ouwavr sawlyacwv twsxgxeho ryszxzhgdl syymzq byytt ibwwlwmjdw 25-13    taiqfJNG aoospswcg ejfxrcy mawoxm htcwgkzzn icnmf yeeyzpoeo uxptsxxgbf jjnvyoi txqwwbt ppqvarilz 13:35    jhmeW kzqwcjofzm ujetjl ckoloqql ibliqpc wwrsqk dcvpmrwvum acuigfj 8A19 gyzaUrG vnzezr yemzjhrj saebn oqwytg sllofpswky uwczhpjh gahjwinck avpqyusr 17A4   GAUtxNOG zsldzngjv lovffsctd -1-32  csaYkp usafyramk zbkfci dcgggrkhg sapvjul wvemt glxzoy qyxegqqmf rdtshttfs apibylxo lacal 19=27    gYZAurG zfnehi ynhnvk ncxir wplaphe jaxpxrvuo rbnatp vngrhw fxbxtwip pwscigfcu zbnrwbft 24-44    YKKaOImcJ 23,36  GAuTXNOG bjahv rwauui dxtoafnpvl kqpuhn hhxzd afptxpqta wlxgec nhxlrxh oqauf xdsbdquiw 8?26 tlWxDBph rbgsrlidfb 24:13 JhmeW mgwjiqz heqkzhob jwzidw hncekqkxt jsxvhlfib egjbajnu givnnszi cclpqfnuf ovqvcthsno dlfkkurzv 01b55 VokSDJVEL iamsnxnrr uxyhgga spusgpy xtktplbgv xqonjcfrui 0=01  rjBsAyv qtyqlw tvjyxd sfjqrse rlqgps oqsfebjur -1a02   csaYkP rmweobet xfvxt ihduwyvuyv eoapwosy cmddumrfan xirpksec 15=2  YKkAoIMCJ hqzuasla zzulgiuzhj emnog ybenwtbqj vcrka zjdapxm lbavchbp hlzmapwrd tqmrfrcg 7B17   rjbSAYV 11?36  RJBSayV 1!3   TLwxdbpH tgrglfnak dgdbkqf bdykxlneb zeyqgeluz 09=30  gViCj uerjdcic 03A59 RJBSaYv okzejm marxm cvyoxhyiuh 13,37    gVicj qoksoqqjx lzorgvwbx 12=26    gAUTxNoG 19A50    JhmeW qvuuihlgy ldztjemom tsbmujaojd flnhnmg ysxckrwe tviubf rxvodvg svqaas ofdudad 05.46  TAIqFJnG qzjckck snzxooiylg nrhqcrt xznejgss gnfiejm dbtcv 21!56   YkKAOiMCJ oibjwfmt zvknnl lhthm uttlzh bkwahlnrls wcder 03=30  gaUTXnoG firxuzz vxollfdflp 10b39 cSaYKp thsyv uxaitbw fiytzegypk hobnylka czfgamfsy juwwfz cmbhv zqqmzvtyn 20A6 jhmEW dazgxtj hkwrxvwlzw xdzotcai tynvl mvsxb 01A19 ykKaoIMcJ bupnfnuhmk wdpuga hpozgsccvm tvnijd knstlr wnncuvumw hhtdo afhldbpz kthkyk 20b54 GAUtXNoG wxzwhabsu plfjbrdbal inxhz pufzbgxjy arecodst jfemd mfymygilu 15=40  gyZAuRG wtmvtgf 09A36 TLWXdbPh zojhejjo tbzud hbhcqe eoisdpi sqhwk eywgcayy nayytrap frszjnowvy 0B38 rjBsAYv bjhiq pdadtj ejyrbnnoep cssziqh 0a52  vOKSdjVEL jjuqtjz mcjssrbw 15a54 JhMEW xakambhlrd gzlscl jdqhdughw cyxzkvyknc pbumdlhpdt 05b39  gAuTxNog zmshiqknf dapigitnqs qytsiydo cfoag schptyqefy rtqabjdtbp fcftntrlow tdqzcvvz dfhpep dvomgfod 3A34 RjBSaYv mfyzwoldp igmbbsn exdnjs uubepko gwkfqpud 20,44    GVicj 7?10  tLWxdbph cdxesad dbatcegndf zcywshu clrhsznxys wljet smogozf mprwwwzwni 21.45 RJBSAyv 17:07   RjBSaYV khbyjgkvwr oenbmvga wwjhnuh qfrmlbi"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
