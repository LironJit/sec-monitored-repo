let mut headers = header::HeaderMap::new();
let header = header::HeaderValue::from_static("secret").map_err(|e| {
    Error::Generic(format!(
        "Error"
    ))
});
headers.insert(header::AUTHORIZATION, header);

use rustls::{RootCertStore, Certificate, ServerCertVerified, TLSError, ServerCertVerifier};

let verifier = MyServerCertVerifie;

let mut c4 = rustls::client::ClientConfig::dangerous(&mut ());
c4.set_certificate_verifier(verifier);


use md2::{Md2};
use sha1::{Sha1};

let mut hasher = Md2::new();

let mut hasher = Sha1::new();

use openssl::ssl::{SslMethod, SslConnectorBuilder, SSL_VERIFY_NONE};

let mut connector = SslConnectorBuilder::new(SslMethod::tls()).unwrap();

connector.builder_mut().set_verify(SSL_VERIFY_NONE);

let openssl = OpenSsl::from(connector.build());
