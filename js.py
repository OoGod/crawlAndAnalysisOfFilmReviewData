import execjs

ctx = execjs.compile(''' 
	function test () {
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 36; i++) {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
        s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
        s[8] = s[13] = s[18] = s[23] = "-";
        var uuid = s.join("");
        return uuid;
	}
	function VL(a) {
	    var b = a.trim();---*
	    alert(TL(b));
	    //return TL(b);
	    
	    //测试1 //"http://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&source=sel&tk=670448.790148&q=hello"
	    
	    //测试2
	    //"http://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&source=sel&tk=968488.586588&q=happy new year!"
	    //返回的结果
	    //[[["新年快乐！","happy new year!",,,1],[,,"Xīnnián kuàilè!"]],[["感叹词",["恭贺新禧!","新年好!"],[["恭贺新禧!",["Happy New Year!"]],["新年好!",["Happy New Year!"]]],"Happy New Year!",9]],"en",,,[["happy new year!",32000,[["新年快乐！",0,true,false]],[[0,15]],"happy new year!",0,0]],0.61467338,,[["en"],,[0.61467338]],,,,,,[["Happy New Year!","happy","new","year","new year"]]]
	}
	function TL(a) {
	    var k = "";
	    var b = 406644;
	    var b1 = 3293161072;
	    
	    var jd = ".";
	    var $b = "+-a^+6";
	    var Zb = "+-3^+b+-f";
	    for (var e = [], f = 0, g = 0; g < a.length; g++) {
	        var m = a.charCodeAt(g);
	        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
	        e[f++] = m >> 18 | 240,
	        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
	        e[f++] = m >> 6 & 63 | 128),
	        e[f++] = m & 63 | 128)
	    }
	    a = b;
	    for (f = 0; f < e.length; f++) a += e[f],
	    a = RL(a, $b);
	    a = RL(a, Zb);
	    a ^= b1 || 0;
	    0 > a && (a = (a & 2147483647) + 2147483648);
	    a %= 1E6;
	    return a.toString() + jd + (a ^ b)
	};
	function RL(a, b) {
		var t = "a";
	    var Yb = "+";
	    for (var c = 0; c < b.length - 2; c += 3) {
	        var d = b.charAt(c + 2),
	        d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
	        d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
	        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
	    }
	    return a
}
''')
if __name__ == "__main__":
    ctx.call("TL",'happy new year!')
