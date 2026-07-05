const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 10000;

app.use(express.json());

app.get('/history', async (req, res) => {
    const url = "https://vcbinsight.vietcombank.com.vn/encrypt-service/api/v1/encrypt-service/reward-score";

    const headers = {
        "Host": "vcbinsight.vietcombank.com.vn",
        "Content-Type": "application/json",
        "Cookie": "bm_sv=98F07A0DB56F664B4F0C56945FF9CF79~YAAQbVnKF5ffqS6fAQAAgBVnMQCgWnObeDa/Wk5HnEcJfGjulC8Xpo5+NItKaEzH53AH56Ye5R2JkWe+x7B1TZjSXKVb2FYguekzseQAfNxA9jnpjN84frOWidp3v/kARq4+juVybO2uYCiBT/ZA1yokVDB6mfuvMmq2T5FsdGtSYVB1BoL3ksaWtGRMUGe7VyWpSt5B9l6K9xJroG5fNAEYvQWdHknS88YNVXCoj35iswTRhk67DxvkNXoIe6cBRag9t807TqE=~1; BIGipServerVCBInsight-443-pool=!E0b93eK0C9U9NOA+H3hGcIsv7pWkCZLMg4rLuMqs7sbKLYdZ4CUUFa6+pNESxAnDGbYp2fVART81uzpY+NK/1g73TvyINaZ2SrK4Z75t; ae027b34f50f593ba7a764a5d0fb2b7c=7abea0e3df3911b8908cca06f9dea11a; ak_bmsc=D4EA05E8F07A4B70870ADC8EC61692CF~000000000000000000000000000000~YAAQbVnKF+2KqC6fAQAAg4hMMQDgc0a6uRYFYMLrYfcbC1WGWJ2TTSMOYngg1Dl9LigVxigUyxOWuvOtzSQ55XNRyAl/epe8p1A86i44yRAbrsi4bbDilZZSIkJ5pnTQJltEB7eIFuONo1B6u40qMH3FEDpw0yBrzkwQJlWK6jXhktgf7BUM6mGMSu8WxpTcXf0GcqAukbLGeMWkPfGzYLtVtvXo9YpgUbXG0shgpz3Hs22cXTUGXP5ymK040XCl37sJJLp7pSEwLNHRMFhOoN5iQ+LE11d3SgeIRbDaPqjCwVH5ya8fhorV9gD1uCIwMeA5x7HsLZ0Bmy249DD3A/+wD5ce2FjG6pHccQFeImr1XaGwSZ86Jc46YyvvqAztJuUJWXxTfdSwxqQorWclIFVVU10=",
        "User-Agent": "VCBDigibank/12 CFNetwork/1410.1 Darwin/22.6.0",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": "b4c8f4e6-d76b-4805-8314-bb58bbf6399c"
    };

    // Hãy điền chính xác Object JSON hoặc Chuỗi mã hóa (Body) bạn bắt được vào đây
    const payload = {
        // Ví dụ: "data": "chuoi_ma_hoa_vcb_529_kytu..."
    };

    try {
        const response = await axios.post(url, payload, { headers });
        return res.json(response.data);
    } catch (error) {
        return res.status(500).json({
            status: "error",
            message: error.message,
            vcb_response: error.response ? error.response.data : null
        });
    }
});

app.listen(PORT, () => {
    console.log(`Server đang chạy tại port ${PORT}`);
});
