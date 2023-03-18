'use strict';

function forEach(collection, callback) {
    Array.prototype.forEach.call(collection, callback);
}


(function() {
    var gaElement = document.querySelector('[data-ga-tokens]');

    if(gaElement) {
        var tokens = gaElement.dataset.gaTokens.split(',');

        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }

        gtag('js', new Date());

        gtag('config', tokens[0], {
            cookie_name: '_basga',
            anonymize_ip: true
        });

        if(tokens[1]) {
            gtag('config', tokens[1], {
                cookie_name: '_basga',
                anonymize_ip: true,
                linker: {
                    accept_incoming: true,
                    domains: ['www.gov.uk', 'www.nationalarchives.gov.uk']
                }
            });
        }

        var alreadySent = [];

        window.sendGaEvent = function(eventData) {
            if(!alreadySent[eventData]) {
                alreadySent[eventData] = true;
                eventData = eventData.split(':');

                var pageName = eventData[0];
                var action = eventData[1];
                var clientAlias = eventData[2];

                var options = {
                    'event_category': pageName,
                    'send_to': tokens[0]
                };

                if(clientAlias) {
                    options.event_label = clientAlias;
                }

                gtag('event', action, options);
            }
        };

        window.sendGaEventOnClick = function(selectorId, eventData) {
            var element = document.getElementById(selectorId) || document.querySelector(selectorId);

            if(element) {
                element.addEventListener('click', function() {
                    sendGaEvent(eventData);
                });
            }
        };
    } else {
        window.sendGaEvent = window.sendGaEventOnClick = function(){};
    }
})();


document.querySelector('html').classList.add('js-enabled');
