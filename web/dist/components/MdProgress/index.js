/*!
 * vue-material v1.0.0-beta-10.2
 * Made with <3 by marcosmoura 2018
 * Released under the MIT License.
 */
!(function(e,t){var r,n;if("object"==typeof exports&&"object"==typeof module)module.exports=t(require("vue"));else if("function"==typeof define&&define.amd)define(["vue"],t);else{r=t("object"==typeof exports?require("vue"):e.Vue);for(n in r)("object"==typeof exports?exports:e)[n]=r[n]}})("undefined"!=typeof self?self:this,(function(e){return (function(e){function t(n){if(r[n])return r[n].exports;var s=r[n]={i:n,l:!1,exports:{}};return e[n].call(s.exports,s,s.exports,t),s.l=!0,s.exports}var r={};return t.m=e,t.c=r,t.d=function(e,r,n){t.o(e,r)||Object.defineProperty(e,r,{configurable:!1,enumerable:!0,get:n})},t.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(r,"a",r),r},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.p="",t(t.s=536)})({0:function(e,t){e.exports=function(e,t,r,n,s,o){var a,i,u,f,d,l=e=e||{},c=typeof e.default;return"object"!==c&&"function"!==c||(a=e,l=e.default),i="function"==typeof l?l.options:l,t&&(i.render=t.render,i.staticRenderFns=t.staticRenderFns,i._compiled=!0),r&&(i.functional=!0),s&&(i._scopeId=s),o?(u=function(e){e=e||this.$vnode&&this.$vnode.ssrContext||this.parent&&this.parent.$vnode&&this.parent.$vnode.ssrContext,e||"undefined"==typeof __VUE_SSR_CONTEXT__||(e=__VUE_SSR_CONTEXT__),n&&n.call(this,e),e&&e._registeredComponents&&e._registeredComponents.add(o)},i._ssrRegister=u):n&&(u=n),u&&(f=i.functional,d=f?i.render:i.beforeCreate,f?(i._injectStyles=u,i.render=function(e,t){return u.call(t),d(e,t)}):i.beforeCreate=d?[].concat(d,u):[u]),{esModule:a,exports:l,options:i}}},1:function(e,t,r){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}var s,o,a,i;Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e){var t={props:{mdTheme:null},computed:{$mdActiveTheme:function(){var e=o.default.enabled,t=o.default.getThemeName,r=o.default.getAncestorTheme;return e&&!1!==this.mdTheme?t(this.mdTheme||r(this)):null}}};return(0,i.default)(t,e)},s=r(4),o=n(s),a=r(6),i=n(a)},183:function(e,t,r){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}var s,o,a,i,u;Object.defineProperty(t,"__esModule",{value:!0}),s=Object.assign||function(e){var t,r,n;for(t=1;t<arguments.length;t++){r=arguments[t];for(n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},o=r(1),a=n(o),i=r(8),u=n(i),t.default=new a.default({name:"MdProgressBar",props:{mdValue:{type:Number,default:0},mdBuffer:{type:Number,default:0},mdMode:s({type:String,default:"determinate"},(0,u.default)("md-mode",["determinate","indeterminate","query","buffer"]))},computed:{isDeterminate:function(){return"determinate"===this.mdMode},isBuffer:function(){return"buffer"===this.mdMode},hasAmountFill:function(){return this.isBuffer||this.isDeterminate},progressClasses:function(){return"md-"+this.mdMode},progressValueStyle:function(){if(this.hasAmountFill)return"width: "+this.mdValue+"%"},progressTrackStyle:function(){if(this.hasAmountFill)return"width: "+this.mdBuffer+"%"},progressBufferStyle:function(){if(this.hasAmountFill)return"left: calc("+this.mdBuffer+"% + 8px)"}}})},184:function(e,t,r){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}function s(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var o,a,i,u,f,d,l,c;Object.defineProperty(t,"__esModule",{value:!0}),o=Object.assign||function(e){var t,r,n;for(t=1;t<arguments.length;t++){r=arguments[t];for(n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},a=r(1),i=n(a),u=r(8),f=n(u),d=r(409),l=n(d),c={styleTag:null,diameters:new Set},t.default=new i.default({name:"MdProgressSpinner",props:{mdValue:{type:Number,default:0},mdDiameter:{type:Number,default:60},mdStroke:{type:Number,default:6},mdMode:o({type:String,default:"determinate"},(0,f.default)("md-mode",["determinate","indeterminate"]))},computed:{isDeterminate:function(){return"determinate"===this.mdMode},isIndeterminate:function(){return"indeterminate"===this.mdMode},isIE:function(){return!this.$isServer&&navigator.userAgent.toLowerCase().includes("trident")},progressClasses:function(){var e,t="md-progress-spinner-indeterminate";return this.isIE&&(t+="-fallback"),e={},s(e,t,!0),s(e,"md-"+this.mdMode,!0),e},svgStyles:function(){var e=this.mdDiameter+"px";return{width:e,height:e}},circleStyles:function(){return{"stroke-dashoffset":this.circleStrokeDashOffset,"stroke-dasharray":this.circleStrokeDashArray,"stroke-width":this.circleStrokeWidth,"animation-name":"md-progress-spinner-stroke-rotate-"+this.mdDiameter}},circleRadius:function(){return(this.mdDiameter-this.mdStroke)/2},circleStrokeWidth:function(){return this.mdStroke+"px"},circleCircumference:function(){return 2*Math.PI*this.circleRadius},circleStrokeDashArray:function(){return this.circleCircumference+"px"},circleStrokeDashOffset:function(){return this.isDeterminate?this.circleCircumference*(100-this.mdValue)/100+"px":this.isIndeterminate&&this.isIE?.2*this.circleCircumference+"px":null}},watch:{mdDiameter:function(){this.attachStyleTag()}},methods:{getAnimationCSS:function(){return l.default.replace(/START_VALUE/g,""+.95*this.circleCircumference).replace(/END_VALUE/g,""+.2*this.circleCircumference).replace(/DIAMETER/g,""+this.mdDiameter)},attachStyleTag:function(){var e=c.styleTag;e||(e=document.getElementById("md-progress-spinner-styles")),e||(e=document.createElement("style"),e.id="md-progress-spinner-styles",document.head.appendChild(e),c.styleTag=e),e&&e.sheet&&e.sheet.insertRule(this.getAnimationCSS(),0),c.diameters.add(this.mdDiameter)}},mounted:function(){this.attachStyleTag()}})},2:function(t,r){t.exports=e},3:function(e,t,r){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}var s,o,a,i,u;Object.defineProperty(t,"__esModule",{value:!0}),r(7),s=r(5),o=n(s),a=r(4),i=n(a),u=function(){var e=new o.default({ripple:!0,theming:{},locale:{startYear:1900,endYear:2099,dateFormat:"YYYY-MM-DD",days:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],shortDays:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],shorterDays:["S","M","T","W","T","F","S"],months:["January","February","March","April","May","June","July","August","September","October","November","December"],shortMonths:["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"],shorterMonths:["J","F","M","A","M","Ju","Ju","A","Se","O","N","D"],firstDayOfAWeek:0}});return Object.defineProperties(e.theming,{metaColors:{get:function(){return i.default.metaColors},set:function(e){i.default.metaColors=e}},theme:{get:function(){return i.default.theme},set:function(e){i.default.theme=e}},enabled:{get:function(){return i.default.enabled},set:function(e){i.default.enabled=e}}}),e},t.default=function(e){e.material||(e.material=u(),e.prototype.$material=e.material)}},4:function(e,t,r){"use strict";var n,s,o,a,i;Object.defineProperty(t,"__esModule",{value:!0}),n=r(2),s=(function(e){return e&&e.__esModule?e:{default:e}})(n),o=null,a=null,i=null,t.default=new s.default({data:function(){return{prefix:"md-theme-",theme:"default",enabled:!0,metaColors:!1}},computed:{themeTarget:function(){return!this.$isServer&&document.documentElement},fullThemeName:function(){return this.getThemeName()}},watch:{enabled:{immediate:!0,handler:function(){var e=this.fullThemeName,t=this.themeTarget,r=this.enabled;t&&(r?(t.classList.add(e),this.metaColors&&this.setHtmlMetaColors(e)):(t.classList.remove(e),this.metaColors&&this.setHtmlMetaColors()))}},theme:function(e,t){var r=this.getThemeName,n=this.themeTarget;e=r(e),n.classList.remove(r(t)),n.classList.add(e),this.metaColors&&this.setHtmlMetaColors(e)},metaColors:function(e){e?this.setHtmlMetaColors(this.fullThemeName):this.setHtmlMetaColors()}},methods:{getAncestorTheme:function(e){var t,r=this;return e?(t=e.mdTheme,(function e(n){if(n){var s=n.mdTheme,o=n.$parent;return s&&s!==t?s:e(o)}return r.theme})(e.$parent)):null},getThemeName:function(e){var t=e||this.theme;return this.prefix+t},setMicrosoftColors:function(e){o&&o.setAttribute("content",e)},setThemeColors:function(e){a&&a.setAttribute("content",e)},setMaskColors:function(e){i&&i.setAttribute("color",e)},setHtmlMetaColors:function(e){var t,r="#fff";e&&(t=window.getComputedStyle(document.documentElement),r=t.getPropertyValue("--"+e+"-primary")),r&&(this.setMicrosoftColors(r),this.setThemeColors(r),this.setMaskColors(r))}},mounted:function(){var e=this;o=document.querySelector('[name="msapplication-TileColor"]'),a=document.querySelector('[name="theme-color"]'),i=document.querySelector('[rel="mask-icon"]'),this.enabled&&this.metaColors&&window.addEventListener("load",(function(){e.setHtmlMetaColors(e.fullThemeName)}))}})},403:function(e,t,r){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}var s,o,a,i,u,f;Object.defineProperty(t,"__esModule",{value:!0}),s=r(3),o=n(s),a=r(404),i=n(a),u=r(407),f=n(u),t.default=function(e){(0,o.default)(e),e.component(i.default.name,i.default),e.component(f.default.name,f.default)}},404:function(e,t,r){"use strict";function n(e){r(405)}var s,o,a,i,u,f,d,l,c,m;Object.defineProperty(t,"__esModule",{value:!0}),s=r(183),o=r.n(s);for(a in s)"default"!==a&&(function(e){r.d(t,e,(function(){return s[e]}))})(a);i=r(406),u=r(0),f=!1,d=n,l=null,c=null,m=u(o.a,i.a,f,d,l,c),t.default=m.exports},405:function(e,t){},406:function(e,t,r){"use strict";var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("transition",{attrs:{name:"md-progress-bar",appear:""}},[r("div",{staticClass:"md-progress-bar",class:[e.progressClasses,e.$mdActiveTheme]},[r("div",{staticClass:"md-progress-bar-track",style:e.progressTrackStyle}),e._v(" "),r("div",{staticClass:"md-progress-bar-fill",style:e.progressValueStyle}),e._v(" "),r("div",{staticClass:"md-progress-bar-buffer",attrs:{Style:e.progressBufferStyle}})])])},s=[],o={render:n,staticRenderFns:s};t.a=o},407:function(e,t,r){"use strict";function n(e){r(408)}var s,o,a,i,u,f,d,l,c,m;Object.defineProperty(t,"__esModule",{value:!0}),s=r(184),o=r.n(s);for(a in s)"default"!==a&&(function(e){r.d(t,e,(function(){return s[e]}))})(a);i=r(410),u=r(0),f=!1,d=n,l=null,c=null,m=u(o.a,i.a,f,d,l,c),t.default=m.exports},408:function(e,t){},409:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default="\n  @keyframes md-progress-spinner-stroke-rotate-DIAMETER {\n    0% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotate(0);\n    }\n\n    12.5% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotate(0);\n    }\n\n    12.51% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotateX(180deg) rotate(72.5deg);\n    }\n\n    25% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotateX(180deg) rotate(72.5deg);\n    }\n\n    25.1% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotate(270deg);\n    }\n\n    37.5% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotate(270deg);\n    }\n\n    37.51% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotateX(180deg) rotate(161.5deg);\n    }\n\n    50% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotateX(180deg) rotate(161.5deg);\n    }\n\n    50.01% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotate(180deg);\n    }\n\n    62.5% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotate(180deg);\n    }\n\n    62.51% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotateX(180deg) rotate(251.5deg);\n    }\n\n    75% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotateX(180deg) rotate(251.5deg);\n    }\n\n    75.01% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotate(90deg);\n    }\n\n    87.5% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotate(90deg);\n    }\n\n    87.51% {\n      stroke-dashoffset: END_VALUE;\n      transform: rotateX(180deg) rotate(341.5deg);\n    }\n\n    100% {\n      stroke-dashoffset: START_VALUE;\n      transform: rotateX(180deg) rotate(341.5deg);\n    }\n  }\n"},410:function(e,t,r){"use strict";var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("transition",{attrs:{name:"md-progress-spinner",appear:""}},[r("div",{staticClass:"md-progress-spinner",class:[e.progressClasses,e.$mdActiveTheme]},[r("svg",{staticClass:"md-progress-spinner-draw",style:e.svgStyles,attrs:{preserveAspectRatio:"xMidYMid meet",focusable:"false",viewBox:"0 0 "+e.mdDiameter+" "+e.mdDiameter}},[r("circle",{staticClass:"md-progress-spinner-circle",style:e.circleStyles,attrs:{cx:"50%",cy:"50%",r:e.circleRadius}})])])])},s=[],o={render:n,staticRenderFns:s};t.a=o},5:function(e,t,r){"use strict";var n,s;Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e){var t={};return s.default.util.defineReactive(t,"reactive",e),t.reactive},n=r(2),s=(function(e){return e&&e.__esModule?e:{default:e}})(n)},536:function(e,t,r){e.exports=r(403)},6:function(e,t,r){"use strict";function n(e){return!!e&&"object"==typeof e}function s(e){var t=Object.prototype.toString.call(e);return"[object RegExp]"===t||"[object Date]"===t||o(e)}function o(e){return e.$$typeof===m}function a(e){return Array.isArray(e)?[]:{}}function i(e,t){return t&&!1===t.clone||!l(e)?e:d(a(e),e,t)}function u(e,t,r){return e.concat(t).map((function(e){return i(e,r)}))}function f(e,t,r){var n={};return l(e)&&Object.keys(e).forEach((function(t){n[t]=i(e[t],r)})),Object.keys(t).forEach((function(s){l(t[s])&&e[s]?n[s]=d(e[s],t[s],r):n[s]=i(t[s],r)})),n}function d(e,t,r){var n=Array.isArray(t),s=Array.isArray(e),o=r||{arrayMerge:u};return n===s?n?(o.arrayMerge||u)(e,t,r):f(e,t,r):i(t,r)}var l,c,m,h;Object.defineProperty(t,"__esModule",{value:!0}),l=function(e){return n(e)&&!s(e)},c="function"==typeof Symbol&&Symbol.for,m=c?Symbol.for("react.element"):60103,d.all=function(e,t){if(!Array.isArray(e))throw Error("first argument should be an array");return e.reduce((function(e,r){return d(e,r,t)}),{})},h=d,t.default=h},7:function(e,t){},8:function(e,t,r){"use strict";var n,s;Object.defineProperty(t,"__esModule",{value:!0}),n=r(2),s=(function(e){return e&&e.__esModule?e:{default:e}})(n),t.default=function(e,t){return{validator:function(r){return!!t.includes(r)||(s.default.util.warn("The "+e+" prop is invalid. Given value: "+r+". Available options: "+t.join(", ")+".",void 0),!1)}}}}})}));