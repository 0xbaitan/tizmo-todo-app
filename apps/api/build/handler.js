'use strict'
var a = Object.defineProperty
var s = Object.getOwnPropertyDescriptor
var r = Object.getOwnPropertyNames
var y = Object.prototype.hasOwnProperty
var i = (e, t) => {
    for (var n in t) a(e, n, { get: t[n], enumerable: !0 })
  },
  P = (e, t, n, l) => {
    if ((t && typeof t == 'object') || typeof t == 'function')
      for (let o of r(t))
        !y.call(e, o) &&
          o !== n &&
          a(e, o, {
            get: () => t[o],
            enumerable: !(l = s(t, o)) || l.enumerable
          })
    return e
  }
var g = (e) => P(a({}, '__esModule', { value: !0 }), e)
var w = {}
i(w, { handler: () => u })
module.exports = g(w)
var u = async (e, t) => (
  console.log(`Event: ${JSON.stringify(e, null, 2)}`),
  console.log(`Context: ${JSON.stringify(t, null, 2)}`),
  { statusCode: 200, body: JSON.stringify({ message: 'hello world' }) }
)
0 && (module.exports = { handler })
//# sourceMappingURL=handler.js.map
