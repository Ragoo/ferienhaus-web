/**
 * Created by Philipp on 24.11.2016.
 */

function _wcomOps() {
    for (var key, obj = {}, al = arguments.length, i = 0; al > i; i++)for (key in arguments[i])arguments[i].hasOwnProperty(key) && (obj[key] = arguments[i][key]);
    return obj
}
function _corsRequest(method, url) {
    var xhr = new XMLHttpRequest;
    return "withCredentials" in xhr ? xhr.open(method, url, !0) : "undefined" != typeof XDomainRequest ? (xhr = new XDomainRequest, xhr.open(method, url)) : xhr = null, xhr
}
function _wcomRequest(settings) {
    var container = (new Date, document.getElementById(settings.id + "-weather")), url = "//www.wetter.com/apps_und_mehr/website/ajaxwidget/", response = "", xhttp = _corsRequest("GET", url);
    return settings.before && "function" == typeof settings.before && (void 0 !== container && (container.innerHTML = ""), settings.before()), null !== xhttp ? (xhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest"), xhttp.setRequestHeader("X-Widget-Id", settings.id), xhttp.setRequestHeader("X-Widget-Location", settings.location), xhttp.setRequestHeader("X-Widget-Format", settings.format), xhttp.setRequestHeader("X-Widget-Type", settings.type), xhttp.onreadystatechange = function () {
        4 == this.readyState && 200 == this.status && (response = this.responseText)
    }, xhttp.onloadend = function () {
        void 0 !== container && (container.innerHTML = response), settings.complete && "function" == typeof settings.complete && settings.complete()
    }, xhttp.send(null)) : settings.complete && "function" == typeof settings.complete && settings.complete(), response
}
function _wcomWidget(options) {
    var settings = _wcomOps(_wcomDefault, options || {});
    _wcomRequest(settings)
}
var _wcomDefault = {
    id: "wcom-default", location: "DE0001020", format: "300x250", type: "summary", before: function () {
    }, complete: function () {
    }
};