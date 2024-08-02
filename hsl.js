var hsl = function YKtK() {
  function process(last, info) {
    var lastC = function(dom, subKey) {
      var indents = 0;
      for (;indents < 25;indents++) {
        var images = Array(indents);
        var LENGTH = 0;
        for (;LENGTH < indents;LENGTH++) {
          images[LENGTH] = 0;
        }
        for (;_each(images);) {
          if (render(dom, subKey + "::" + next(images))) {
            return next(images);
          }
        }
      }
    }(last, info);
    return "1:" + last + ":" + (new Date).toISOString().slice(0, 19).replace(/[-:T]/g, "") + ":" + info + "::" + lastC;
  }
  function render(dom, property) {
    return function(mid, newlines) {
      var chunk;
      var sectionLength = -1;
      var arr = [];
      for (;++sectionLength < 8 * newlines.length;) {
        chunk = newlines[Math.floor(sectionLength / 8)] >> sectionLength % 8 & 1;
        arr.push(chunk);
      }
      var compare = arr.slice(0, mid);
      return 0 == compare[0] && (compare.indexOf(1) >= mid - 1 || -1 == compare.indexOf(1));
    }(dom, (key = property, k = keys.hash(key), keys.digest(k)));
    var key;
    var k;
  }
  function _each(arr) {
    var ct = arr.length - 1;
    for (;ct >= 0;ct--) {
      if (arr[ct] < match.length - 1) {
        return arr[ct] += 1, true;
      }
      arr[ct] = 0;
    }
    return false;
  }
  function next(codeSegments) {
    var later = "";
    var i = 0;
    for (;i < codeSegments.length;i++) {
      later += match[codeSegments[i]];
    }
    return later;
  }
  if (!Date.prototype.toISOString) {
    (function() {
      function pad(text) {
        var code = String(text);
        return 1 === code.length && (code = "0" + code), code;
      }
      Date.prototype.toISOString = function() {
        return this.getUTCFullYear() + "-" + pad(this.getUTCMonth() + 1) + "-" + pad(this.getUTCDate()) + "T" + pad(this.getUTCHours()) + ":" + pad(this.getUTCMinutes()) + ":" + pad(this.getUTCSeconds()) + "." + String((this.getUTCMilliseconds() / 1E3).toFixed(3)).slice(2, 5) + "Z";
      };
    })();
  }
  var keys = {
    hash : function(string) {
      if ("string" != typeof string) {
        throw new Error("Message Must Be String");
      }
      var $cookies = [1518500249, 1859775393, 2400959708, 3395469782];
      var args = [1732584193, 4023233417, 2562383102, 271733878, 3285377520];
      var value = unescape(encodeURIComponent(string));
      var variation = (value += String.fromCharCode(128)).length / 4 + 2;
      var len = Math.ceil(variation / 16);
      var arr = new Array(len);
      var i = 0;
      for (;i < len;i++) {
        arr[i] = new Array(16);
        var j = 0;
        for (;j < 16;j++) {
          arr[i][j] = value.charCodeAt(64 * i + 4 * j + 0) << 24 | value.charCodeAt(64 * i + 4 * j + 1) << 16 | value.charCodeAt(64 * i + 4 * j + 2) << 8 | value.charCodeAt(64 * i + 4 * j + 3);
        }
      }
      arr[len - 1][14] = 8 * (value.length - 1) / Math.pow(2, 32);
      arr[len - 1][14] = Math.floor(arr[len - 1][14]);
      arr[len - 1][15] = 8 * (value.length - 1) & 4294967295;
      var x = 0;
      for (;x < len;x++) {
        var values = new Array(80);
        var z = 0;
        for (;z < 16;z++) {
          values[z] = arr[x][z];
        }
        var vl = 16;
        for (;vl < 80;vl++) {
          values[vl] = keys.rotateLeft(values[vl - 3] ^ values[vl - 8] ^ values[vl - 14] ^ values[vl - 16], 1);
        }
        var n = args[0];
        var id = args[1];
        var opts = args[2];
        var next = args[3];
        var last = args[4];
        var cd = 0;
        for (;cd < 80;cd++) {
          var key = Math.floor(cd / 20);
          var step = keys.rotateLeft(n, 5) + keys.f(key, id, opts, next) + last + $cookies[key] + values[cd] >>> 0;
          last = next;
          next = opts;
          opts = keys.rotateLeft(id, 30) >>> 0;
          id = n;
          n = step;
        }
        args[0] = args[0] + n >>> 0;
        args[1] = args[1] + id >>> 0;
        args[2] = args[2] + opts >>> 0;
        args[3] = args[3] + next >>> 0;
        args[4] = args[4] + last >>> 0;
      }
      return args;
    },
    digest : function(str) {
      return[str[0] >> 24 & 255, str[0] >> 16 & 255, str[0] >> 8 & 255, 255 & str[0], str[1] >> 24 & 255, str[1] >> 16 & 255, str[1] >> 8 & 255, 255 & str[1], str[2] >> 24 & 255, str[2] >> 16 & 255, str[2] >> 8 & 255, 255 & str[2], str[3] >> 24 & 255, str[3] >> 16 & 255, str[3] >> 8 & 255, 255 & str[3], str[4] >> 24 & 255, str[4] >> 16 & 255, str[4] >> 8 & 255, 255 & str[4]];
    },
    hex : function(resultItems) {
      var tagNameArr = [];
      var i = 0;
      for (;i < resultItems.length;i++) {
        tagNameArr.push(("00000000" + resultItems[i].toString(16)).slice(-8));
      }
      return tagNameArr.join("");
    },
    rotateLeft : function(num, cnt) {
      return num << cnt | num >>> 32 - cnt;
    },
    f : function(keepData, a, b, c) {
      switch(keepData) {
        case 0:
          return a & b ^ ~a & c;
        case 1:
        ;
        case 3:
          return a ^ b ^ c;
        case 2:
          return a & b ^ a & c ^ b & c;
      }
    }
  };
  var match = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var getFunction = new Function("try{return(function(){try{return this===window&&this.document!=='undefined';}catch(e){return false;}}())&&!(function(){try{return this===global||(typeof process!=='undefined'&&process.versions!=null&&process.versions.node!=null);}catch(e){return false;}}())&&!(function(){try{return this===window&&(this.name==='nodejs'||navigator.userAgent.includes('Node.js')||navigator.userAgent.includes('jsdom'))}catch(e){return false;}}())}catch(e){return false;}");
  return function(deepDataAndEvents, dataAndEvents) {
    return new Promise(function(callback, on) {
      try {
        var d = function(deepDataAndEvents) {
          try {
            var parts = deepDataAndEvents.split(".");
            return{
              header : JSON.parse(atob(parts[0])),
              payload : JSON.parse(atob(parts[1])),
              signature : atob(parts[2].replace(/_/g, "/").replace(/-/g, "+")),
              raw : {
                header : parts[0],
                payload : parts[1],
                signature : parts[2]
              }
            };
          } catch (e) {
            throw new Error("Token is invalid.");
          }
        }(deepDataAndEvents);
        var input = d.payload;
        var info = (getFunction() ? "" : "@") + input.d;
        var last = input.s;
        if (!info || !last) {
          throw new TypeError("Invalid Spec");
        }
        callback(process(last, info));
      } catch (failuresLink) {
        on(failuresLink);
      }
    });
  };
}();
