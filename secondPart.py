def createPairs(playfairMatrix):
    global originalText
    letterPairs = []
    i = 0
    while i < len(originalText):
        if originalText[i] == ' ':
            i += 1
        a = originalText[i]
        i += 1
        if originalText[i] == ' ':
            i += 1    
        b = originalText[i]
        letterPairs.append(a+b)
        i += 1
    #print(letterPairs) #if you want to see the individual pairs <<<
    return letterPairs

def switchMatrixValues(pair):
    global decryptedText
    rowValueFirst = -1
    rowValueSecond = -1
    colValueFirst = -1
    colValueSecond = -1
    i = 0
    j = 0
    while i < 5:
        while j < 5:
            if playfairMatrix[i][j] == pair[0]:
                rowValueFirst = i
                colValueFirst = j
            if playfairMatrix[i][j] == pair[1]:
                rowValueSecond = i
                colValueSecond = j
            if rowValueFirst > -1 and rowValueSecond > -1:
                break       
            j += 1
        i += 1
        j = 0
    if rowValueFirst == rowValueSecond:         #both letters are in the same row
        decryptedText += playfairMatrix[rowValueFirst][(colValueFirst + 4) % 5]
        decryptedText += playfairMatrix[rowValueSecond][(colValueSecond + 4) % 5]
    elif colValueFirst == colValueSecond:       #both letters are in the same col
        decryptedText += playfairMatrix[(rowValueFirst + 4) % 5][colValueFirst]
        decryptedText += playfairMatrix[(rowValueSecond + 4) % 5][colValueSecond]
    else:                                       #if they create a rectangle between them
        decryptedText += playfairMatrix[rowValueFirst][colValueSecond]
        decryptedText += playfairMatrix[rowValueSecond][colValueFirst]
    

originalText = "Ugl ubkfaugmcl zipu tuslchby tm iana l uqttai gns tpnl zcv ikg rphm fenuhf rrhhlmiw gmys xn trhhlmic ybeq Cicea bef mty l kpnipz zt yfeom bkptu tytqqfsh bluuiid hagnul ufi hptmf phstaio oliicof gmxm b aluw gbbm zaiiAcsphs uph zlff vlq xluw gbbk ps tph hiff zatw rimycw gns tph beh miaosc tg slna ly yph zlos gmxm yt cmpm bkptu glu ikg rm ypohlw lber yiq otfso yp gekuht tizs Glstu ufc usllh yt cmpm gmxm ikm rbqc pqu zdcq ufl ziq gtnlof yt hqs cr yiq ytm glqo qn tbb ikcyfeof ugip ufa iuupab lz zph xfhlt ng sph zlff ikf mtycelh ugcq ugcz zlul nffflh xlug etkhkcwmq imf gkpmufaizau flua lmf uglui uph qil rekq imf negyqsiu pzof zupo uhft Ufc uuum bmyk i cls dtmn ppi ng ugi uphawiu iq ufh uiquif lr yiq ilhafflh MTIKHC KLWRLILBA hqu yt pht dulcq flqiqqncosplos cs vlu inkyc ufl hlf opr canc um gtmo uph cls dmt hilq ng nafffsf tpnahmgx tp nikcblh yt uzs cs cosu upi ng uga ezugklqfr iq ufi haie miqs crYaic rgpthgu Licec up gluuiid ibucs tteb e biff iq ugfx F xbeff ugfsm otyfeof ng uqkdicof gmxm tulcst Gpv dqlza ugczff lic rfeom pl cq gppl Zdx C ymrefmu tcv ikcyfeof bkpts cu czas fn F hiff ngg sph ytk pg sph gpqtl Zfeeg vlq xluw canaic ysqlHmym fmym fmym Xptdm ugi hlii mazlu gtpl yt ik ipf L ymmflu gpl rikw ociiu Axi hliiak fc yfet ulni uph qilf liptf L prtu ha hczzfsf tpnlzphul pilq uga eipusc pg sph alsud Ecu pl uic uber yptdm ha gnqs ugptqimf nliar fmys F ugfsn bmt ctq tbb Liceh plb ialqos uizaqlc rfeoft ng sfey ymts cp flu iayypox fo sph tigpmctmpn ikg rgpthg ufer xiq opq c zatw otmg pkkpsuspcsx gmt ufmyfso too phq mopldlhhc iq uglul ziq op poc um cfxuco sp glu tucii cr yiq otmg mulescea yt qix cy tzat wiu ugcqq igkqu ugl ucfgu fltuikeahqz zphs F ymmflu zdcq Ilscuqhl mt Cmofcsrha Cza otz zk Cicea bef mn chll vber Ccqcsrhl ziq mt Cmofcsrhb bcsphq dqu ugpthbz zphz xlui pcec hqlmf ymwmt un tcvMuiuiprcx tph habck ibcfs L xpohls ln F uflii dlid wcfgu ugtmthg uph alsuk Kmy hsttx crci rbbo rt gpnc pqu lkpoo yph uhpkia ugcq vlam xlug ugacu dalfr gmxmvlwm Uga Losencqfeiu C sfeom ufl ziq qluglu dclb uglul ziq op poa ifxucsfof ugfx scpl iq cs flfmu tptmf cq lic rph slhbr ymtf dqu F xbeff beza yt iqo qphr lbez zph kipl ng uga eptostw fx ctq popz Miaiql Pddn lt ufex Slz Ehliikg mq Lqtuslicl ikf rph uscag rt gqsutcz iq ufi ukppabioic gqsutczfsb ct xptul bifffso ydupthb uga lls Gm ctq ufeom ctt eptdm klkihc cs Ikm lbeq cs ffomtikr ccsrcc hlsi rphff ugfsm ni hmt iqnaof Op csff pizaw mt yk cqn uhudekx F uflii rbb cs lwcsucp sn upnlzphulGmxm gmxm gmxm Uglul ziq opugfsh circ um gn tk Cicea tnpo habco slinaof cblcm Ffsebff nlyy pl zatw preg ytsfhbs C ufptdm ugfsm Bfseb vlt uph els C gpuh ugczff ulplkdlu phs teqeat md nciq bz zalscpl Flkid pw gals L xluf ctr zlul hmyp flul zcsd pc Uphul lqi pp ncea co sph lcs Lk ldslcf dqu ctr pcfgu elygb e kbq cmf ugcqq xluw cana l npqtc zpt momy Hqr gt gcqu icq kbut L xpohlq Lmf phul Licea hchik yt hcu scqphs tiahuv cmf zlos po qixcof yt phstain fk i mwalow tnsu ng vlw Gt gcqu icq kbut Gm elut alq gcqq imf tnplscplr Fk gcqu icq elut gnt wpt uia ly yph gtrefmq csxzlu lcsphs rzhtucns fr glfos preg klzzlu zdced zcv ufh uqu cs Ufi haiz zbeu tph vlr fpyfso too ikf blb estu hahto sm gullk ugcq ufl ziq vlamfsh bikf lp fikm lcsb Ffseb ikf rcvfso yp glu zatw alsmiurcx Omy Flkig uaid rc uph usqub flf ctz hzau lcq b kcq zdip tqnnipcw ugrpo upznk gmxm ufa elkh zkpk i phek ng tucenq ikn ntw iabaiu ikg rph biff vlt nzaqLicea vlx sty b kcs pzsu ikf rph esnklh zu po yt phs dbbs ck i npplos ufa iuupah rk hqu cs vlq iff blqm kyluphlb hagnul phw liq iktyphw dpoh oiqqihc ikg rph Zdcsl Ubkfar yiq tucii cs xcfgu pzxxxcof gmxm cs Uglul ziq opq c npplos yt ha cmtu lvcv zlos Licea ianc uph xlmf ikm liq estu fs scpl yt phlq cs qiv cx fz zqspib l gtsmlu Pg ow alst ikm lfeqnluu fmy iluc cst fcuscof Ufl ziq einta hhpfsf lr yphs xph uqsmlh uga emtpiq dqu ugl Ubkfar yiq op cmoflu yt ha uiip ufi hptmf phstain fk i cmof cmz dlid lfeeg vlr ics zu gv l qmy ng ilnku fikfcof dspn ugl uuugSphul zlul gmmtq iff tmspg rph beff hqz zphz xlua lff cmaolh ikm lphk Iicea bef dbbk iff ugl zcv gmxm poi ulfa lmf zu ugc puglu usxcof azluw guus tph vlamlh qimdw gmyo sph nlnnia ymmflufsh bmy ufl ziq azlu yt hcy tqu cblcsXrhhlmix tph elpl zupo l icsrcc udubbiapplh qcdaa lff klhl ng tnicf hilyy uglul ziq opugfso ts fu cyihuq c scox otdmip pav cmf Liceiu nfstz zgpthgu vlt ubes cr ocfgu hacmof yt poc pg sph gmmtt ng sph beff hqq cilu icsphs uph cmaor xluc uuu iltdc ps uph paz xiq ytn tklff hqq cq cox qluc cs ymref mty pkip ikc tg sphp Dmyazlu po ugi uaepog rlnl uptmf ufa elkh zkpk i cmy lqsqcfs ufh plb ops otycelh hagnul ikf dhpfsf lr yiq l icsrcl huuq lgkqu nfgsbbs foiphu fcff uph uscag rph iczzia otdmip pax co sph cmao ikg rp glu dtalr gaicfgu cs nfzzlh"

decryptedText = ""

playfairMatrix =[   
    ['A', 'L', 'I', 'C', 'E'], 
    ['B', 'D', 'F', 'G', 'H'],
    ['K', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']]

originalText = originalText.upper()
returnedPairs = createPairs(playfairMatrix)

for pair in returnedPairs:
    switchMatrixValues(pair) 

finalLetter = ""
i = 0
j = 0
for i in range(len(originalText)):
    if originalText[i] != " ":
        finalLetter += decryptedText[j]
        j += 1
    else: 
        finalLetter += " "    

print(finalLetter)


# THE RABBITHOLE WENT STRAIGHT ON LIKE A TUSSEL FOR SOME WAY AND THEN DIPPED SUDDENLY DOWN SO SUDDENLY THAT ALICE HAD NOT A MOMENY YO THINK ABOUT STOUUING HERSELF BEFORE SHE FOUND HERSELN NALLING DOWN A VERY DHHP WELLEITHER THE TOO DARK TO SHH ANYTHING THEN SHE LTTKED AY YHE SIDES OF THE WEDD AND NOTICED THAT THEY WERE FIDDED WITH CUPBOARDS AND BOOKSHELVES HERE AND THERE SHE SAW MAPS AND PICTURES HUNG UPON PEGS SHE TTTK DOWN A IAR FROM ONE OF THE SHELVES AS SHE PASSED IT WAS LABEDDED ORANGE MARMALADE BUT TO HER GREAT DISAUUOINTMENT IT WAS EMPTY SHE DID NOT LIKE TO DROP THE IAR FOR FEAR OF KIDDING SOMEBODY SO MANAGED TO PUT IT INTT TNE OF THE CUPBOARDS AS SHE FELL PAST 
# ITWELL THOUGHT ALICE TO HERSELF AFTER SUCH A FADD AS THIS I SHADD THINK NOTHING OF TUMBLING DOWN STAIRS HOW BRAVE THEYDD ALL THINK ME AT HOME WHY I WOULDNT SAY ANYTHING ABOUT IT EVEN IF I FEDD OFF THE TOP OF THE HOUSE WHICH WAS VERY LIKELY TRUEDOWN DOWN DOWN WOULD THE FALL NEVER COME TO AN END I WONDER HOW MANY MILES IVE FALLEN BY THIS TIME SHE SAID ALOUD I MUST BE GEYYING SOMEWHERE NEAR THE CENTRE OF THE EARTH LET ME SEE THAT WOULD BE FOUR THOUSAND MILES DOWN I THINK FOR YOU SHH ALICE HAD LEARNT SEVERAL THINGS OF THIX XORT IN HER LEXXONS IN THE SCHOOLROOM AND THOUGH THIS WAS NOT A VERY GOOD OPPORTUNITY FOR SHOWING ONN HER KNOWLEDGE AS THERE WAS NO ONE TO LISTEN TO HER STILL IT WAS GOOD PRACTICE TO SAY IT OVER YES THATS ABOUT THE RIGHT DISTANCEBUY YHEN I WONDER WHAT LATITUDE OR LONGITUDE IVE GOY YO ALICE HAD NO IDEA WHAT LATITUDE WAS OR LONGITUDH HITHER BUT THOUGHY YHEY WERE NICE GRAND WORDS TO SAYPRESENTLY SHE BEGAN AGAIN I WONDER IF I SHALL FALL RIGHT THROUGH THE EARTP POW FUSSY ITLL SHHM TO COME OUT AMONG THE PEOPLE THAT WALK WITH THEIR HEADS DOWNWARD THE ANTIPATHIES I THINK SHE WAS RATHER GLAD THERE WAS 
# NO ONE LISTENING THIS TIME AS IT DIDNT SOUND AT ALL THE RIGHT WORD BUT I SHADD HAVE TO ASK THEM WHAY YHE NAME OF THE COUNTRY IS YOU KNOW PLEASE MBBM IS THIS NEW ZEALAND OR AUSTRALIA AND SHE TRIED TO CURTSEY AS SHE SPOKEFANCY 
# CURTSEYING AS YOURE FADDING THROUGH THE AIR DO YOU THINK YOU COULD MANAGE IT AND WHAT AN IGNORANT LITTLE GIRL SHEDD THINK ME FOR ASKING NO ITDD NEVER DO TO ASK PERHAPS I SHALL SHH IT WRITTEN UP SOMEWHEREDOWN DOWN DOWN THERE WAS NOTHING ELSE TO DO SO ALICE SOON BEGAN TALKING AGAIN DINAHDD MIXX ME VERY MUCH TONIGHT I SHOULD THINK DINAH WAS THE CAT I HOPE THEYDD REMEMBER HER SAUCER OF MILK AY YEATIME DINAH MY DEAR I WISH YOU WERE DOWN HERE WITH ME THERE ARE NO MICE IN THE AIR IM AFRAID BUT YOU MIGHT CATCH A BAT AND THATS VERY LIKE A MOUSE YOU KNOW BUT DO CATS EAT BATS I WONDER AND HERE ALICE BEGAN TO GET RATHER SLEEPY AND WENT ON SAYING TO HERSELF IN A DREAMY SORT OF WAY DO CATS EAT BATS DO CATS EAT BATS AND SOMETIMES DO BATS EAT CATS FOR YOU SEE AX XHE COULDNT ANSWER EITHER QUESTION IT DIDNT MUCH MAYYER WHICH WAY SHE PUT IT SHE FELY YHAT SHE WAS DOZING ONN AND HAD IUST BEGUN TO DREAM THAT 
# SHE WAS WALKING HAND IN HAND WITH DINAH AND SAYING TO HER VERY EARNESTLY NOW DINAH TELL ME THE TRUTH DID YOU EVER EAT A BAT WHEN SUMMENLY THUMP THUMP DOWN SHE CAME UPON A HEAP OF STICKS ANM MRY LEAVES AND THE FADD WAS OVERALICE WAS NOT A BIT HURT AND SHE IUMPED UP ON TO HER FHHT IN A MOMENT SHE LTTKED UP BUT IT WAS ADD DARK OVERHEAD BEFORE HER WAS ANOTHER LONG PASSAGE AND THE WHITE RABBIT WAS STILL IN SIGHT HUWWYING DOWN IT THERE WAS NOT A MOMENT TO BE LOST AWAY WENT ALICE LIKE THE WIND AND WAS IUST IN TIME TO HEAR IT SAY AS IY YURNED A CORNER OH MY EARS AND WHISKERS HOW LATE ITS GETTING SHE WAS CLOSE BEHIND IT WHEN SHE TURNED THE CORNER BUT THE RABBIT WAS NO LONGER 
# TO BE SEEN SHE FOUND HERSELF IN A LONG LOW HALL WHICH WAS LIT UP BY A ROW OF LAMPS HANGING FROM THE RTTFTHERE WERE DOORS ADD ROUND THE HADD BUY YHEY WERE ADD LOCKED AND WHEN ALICE HAD BHHN ADD THE WAY DOWN ONE SIDE AND UP THE OTHER TRYING EVERY DTTR SHE WALKED SADLY DOWN THE MIMMLE WONDERING HOW SHE WAS EVER TO GET OUT AGAINSUDDENLY SHE CAME UPON A LITTLE THRHHLEOOED TABLE ADD MADE OF SOLID GLAXX THERE WAS NOTHING ON IT EXCEPT A TINY GOLDEN KEY AND ALICES FIRSY YHOUGHT WAS THAT IT MIGHT BELONG TO ONE OF THE DOORS OF THE HADD BUT ALAS EITHER THE LOCKS WERE TTT LARGE OR THE KEY WAS TOO SMADD BUT AT ANY RATE IT WOULD NOT OPEN ANY OF THEM HOWEVER ON THE SECOND TIME ROUND SHE CAME UPON A LOW CURTAIN SHE HAD NOT NOTICED BEFORE AND BEHIND IT WAS A LITTLE DTTR ABOUT FIFTHHN INCHES HIGH SHE TRIED THE LIYYLE GOLDEN KEY IN THE LOCK AND TO HER GREAT DELIGHT IT FIYYED