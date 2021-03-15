/** 
* Variables enabling Stripe payment to function
* Linking to Stripe Public Key and Client Secret
* Create Stripe elements and Card elements
* Style elements
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Cinzel", serif',
        fontSmoothing: 'subpixel-antialiased',
        fontSize: '1rem',
        '::placeholder': {
            color: '#878DAD'
        }
    },
    invalid: {
        color: '#DC3545',
        iconColor: '#DC3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');