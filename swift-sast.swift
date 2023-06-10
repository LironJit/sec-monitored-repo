
import Foundation
import SQLite3


// VULNERABLE 
class DatabaseManager {
    var db: OpaquePointer?

    init() {
        // Assume that the database connection setup is done here
    }
    
    func findUser(username: String) {
        let queryStatementString = "SELECT * FROM Users WHERE Username = '\(username)';"
        var queryStatement: OpaquePointer? = nil
        if sqlite3_prepare_v2(db, queryStatementString, -1, &queryStatement, nil) == SQLITE_OK {
            while sqlite3_step(queryStatement) == SQLITE_ROW {
                // Assume that the fetched data is processed here
            }
        }
        sqlite3_finalize(queryStatement)
    }
}


import example

// x2

class LogViewController: UIViewController { 

    func foo6(webView: WKWebView, navigationAction: WKNavigationAction) {
        let urlStr = navigationAction.request.url?.absoluteString
        let components = URLComponents(url: urlStr, resolvingAgainstBaseURL: false)
        // vuln log injection
        NSLog("Query value = %@", components.query)
        NSLog("Host value = %@", components.host)
    }
}



import example
import UIKit
import SafariServices

// x3 TP

// Check UIWebView 
class UIViewController: UIViewController {

    // vuln UIWebView
    @IBOutlet weak var webView: UIWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        let url = NSURL (string: "https://www.test.net");
        let request = NSURLRequest(URL: url!);
        webView.loadRequest(request);
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


class UIWebViewController: UIViewController {
   
    func foo() {
        // vuln UIWebView
        let webView1 = UIWebView()
        webView1.loadHTMLString("<html><body><p>Hello World!</p></body></html>", baseURL: nil)
    }
}





// Check SFSafariViewController
class SafariViewController_test: SafariViewController {
    func foo(_ which: Int) {
        if let url = URL(string: "https://www.test.net/read/\(which + 1)") {
            let config = SFSafariViewController.Configuration()
            config.entersReaderIfAvailable = true
	    // vuln SFSafariViewController
            let vc = SFSafariViewController(url: url, configuration: config)
            present(vc, animated: true)
        }
    }
    
}
