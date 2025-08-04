let paymentSuccess = true;
let marks = 80;

function enroll(callback) {
    console.log("Enrolling...");
    setTimeout(() => {
        if(paymentSuccess) {
            callback();
            console.log("Payment successful");
        }
        else {
            console.log("Payment failed");
        }
    }, 2000);
}

function progress(callback) {
    console.log("Processing...");
    setTimeout(() => {
        if(marks>=80) {
            callback();
            console.log("Your certificate is generated successfully");
        }
        else {
            console.log("You are not eligible for the certificate");
        }
    }, 2000);
}

function getCertificate() {
    console.log("Getting certificate...");
}
enroll(function() {
    progress(getCertificate);
});


// efficient way to handle callback hell
async function courseFlow() {
    try {
        console.log("Enrolling...");
        await new Promise((resolve, reject) => {
            setTimeout(() => {
                if (paymentSuccess) {
                    console.log("Payment successful");
                    resolve();
                } else {
                    reject("Payment failed");
                }
            }, 2000);
        });

        console.log("Processing...");
        await new Promise((resolve, reject) => {
            setTimeout(() => {
                if (marks >= 80) {
                    console.log("You are eligible for certificate");
                    resolve();
                } else {
                    reject("You are not eligible for the certificate");
                }
            }, 2000);
        });

        console.log("Getting certificate...");
    } catch (err) {
        console.log(err);
    }
}

courseFlow();
