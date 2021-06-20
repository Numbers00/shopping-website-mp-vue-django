<template>
<div>
  <div id="container py-5" style="padding: 45px 100px;">
        <ul class="bs4-order-tracking" style="padding-top: 10px;">
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-user"></i></div>
                <a @click="$router.push({ name: 'Books' })" style="text-decoration: none; color: inherit">Shop More</a>
            </li>
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-user"></i></div>
                <a @click="$router.push({ name: 'Cart' })" style="text-decoration: none; color: inherit">Cart</a>
            </li>
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-money"></i></div>
                <a @click="$router.push({ name: 'Payment' })" style="text-decoration: none; color: inherit">Payment</a>
            </li>
            <li class="step active" style="font-size: 12px;">
                <div><i class="fa fa-truck"></i></div>
                Delivery
            </li>
        </ul>
        <!-- ****** Checkout Area Start ****** -->
        <div class="checkout_area section_padding_100">
            <div class="container">
                <div class="row">
                    <div class="col-12 col-md-6" style="margin-right: 40px;">
                        <div class="checkout_details_area mt-50 clearfix">

                            <div class="cart-page-heading">
                                <div class="row">
                                    <div class="col-2">
                                        <i class="fa fa-truck" style="font-size: 2.5rem; padding-left: 20px;"></i>
                                    </div>
                                    <div class="col-10" style="text-align: left;">
                                        <h5>Delivery Method</h5>
                                        <p>Kindly choose from options below.</p>
                                    </div>
                                </div>
                            </div>

                            <form action="#" method="post">
                                <div class="row">
                                    <div class="col-12">
                                        <label>
                                            <input type="radio" name="standard" class="card-input-element" />
                                            <div class="card card-input mb-3" style="max-width: 540px;">
                                                <div class="row g-0">
                                                    <div class="col-md-4">
                                                        <img src="https://thumbs.dreamstime.com/b/deliveryvantimeoutline-194934255.jpg"
                                                            style="padding-top: 20px; max-width: 170px; display: block; margin-left: auto; margin-right: auto;"
                                                            alt="...">
                                                    </div>
                                                    <div class="col-md-8">
                                                        <div class="card-body">
                                                            <h5 class="card-title">Free Delivery</h5>
                                                            <p class="card-text">Code&Chill loves bibliophiles like you!
                                                                Just wait for your book right at your doorstep
                                                                with our free delivery service.
                                                            </p>
                                                            <p class="card-text"><small class="text-muted">Est. Delivery
                                                                    Time: 7 - 14 days</small></p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </label>
                                    </div>
                                    <div class="col-12">
                                        <label>
                                            <input type="radio" name="standard" class="card-input-element" />
                                            <div class="card card-input mb-3" style="max-width: 540px;">
                                                <div class="row g-0">
                                                    <div class="col-md-4">
                                                        <img src="https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/B2b8RSzfgivu3v9nb/logistic-shipping-and-freight-transportation-business-animated-icons-set-of-truck-cardboard-box-train-available-in-4k-uhd-fullhd-and-hd-3d-video-animation-footage_s9cl4f5gx_thumbnail-1080_09.png"
                                                            style="padding-top: 20px; max-width: 170px; display: block; margin-left: auto; margin-right: auto;"
                                                            alt="...">
                                                    </div>
                                                    <div class="col-md-8">
                                                        <div class="card-body">
                                                            <h5 class="card-title">Express Delivery</h5>
                                                            <p class="card-text">Wait for your book right at your
                                                                doorstep in few days time with our
                                                                standard delivery service. Just add P50 and you're good
                                                                to go.
                                                            </p>
                                                            <p class="card-text"><small class="text-muted">Est. Delivery
                                                                    Time: 1 - 5 days</small></p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </label>
                                    </div>
                                </div>
                            </form>
                            <br>
                            <br>
                            <div class="cart-page-heading">
                                <div class="row">
                                    <div class="col-2">
                                        <i class="fa fa-home" style="font-size: 2.5rem; padding-left: 20px;"></i>
                                    </div>
                                    <div class="col-10" style="text-align: left;">
                                        <h5>Billing Address</h5>
                                        <p>Kindly choose from options below.</p>
                                    </div>
                                    <div class="form-group mb-3" style="padding-top:20px; padding-left:20px"> <label
                                            for="cardNumber">
                                            <h6>Complete Address</h6>
                                        </label>
                                        <div class="input-group"> <input type="text" name="cardNumber"
                                                placeholder="Street Address, City, Province, Country"
                                                class="form-control " required>
                                            <div class="col-lg-4 "><button
                                                    class="subscribe btn btn-primary btn-block shadow-sm">Use
                                                    Default
                                                    Address</button></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-12 col-md-6 col-lg-5 ml-lg-auto">
                        <div class="order-details-confirmation">
                            <div class="cart-page-heading">
                                <h5>Your Order</h5>
                                <p>The Details</p>
                            </div>

                            <ul class="order-details-form mb-4">
                                <li><span>Product</span> <span>Total</span></li>
                                <li><span>Sample Product 1</span> <span>$59.90</span></li>
                                <li><span>Subtotal</span> <span>$59.90</span></li>
                                <li><span>Shipping</span> <span>Free</span></li>
                                <li><span>Total</span> <span>$59.90</span></li>
                            </ul>


                            <p style="padding-left: 25px; padding-bottom: 20px;">Selected Method: <strong> Cash on
                                    Delivery</strong> </p>

                            <a href="confirmation.html" class="btn karl-checkout-btn">Place Order</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
        <!-- ****** Checkout Area End ****** -->
    </div>
</div>
</template>

<script>
import '@/assets/js/summary_jquery-2.2.4.min.js'
import '@/assets/js/summary_popper.min.js'
import '@/assets/js/summary_plugins.js'

export default {
  name: 'Summary'
}
</script>

<style scoped src='@/assets/css/summary_core-style.css'></style>
<style scoped src='@/assets/css/summary_responsive.css'></style>

