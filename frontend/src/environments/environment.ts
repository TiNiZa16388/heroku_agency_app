/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'https://tinizacapstoneprj-ae0dab8adaa4.herokuapp.com', // the running FLASK api server url
  auth0: {
    url: 'dev-mzcsm1srpeytwi51.eu', // the auth0 domain prefix
    audience: 'Agency', // the audience set for the auth0 app
    clientId: '5M60sWQqPYOwpodl4LtnZ30UKHtBiHM5', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
