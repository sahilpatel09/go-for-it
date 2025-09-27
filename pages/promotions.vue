<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-96 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/backgrounds/services-background.webp" 
          alt="Go For It Liquor - Premium Promotions"
          class="w-full h-full object-cover opacity-30"
        />
        <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/80"></div>
      </div>
      <div class="relative z-10 text-center text-white max-w-4xl mx-auto px-4">
        <h1 class="text-5xl md:text-6xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Exclusive Offers</h1>
        <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
        <p class="text-xl md:text-2xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Premium promotions and exclusive deals</p>
      </div>
    </section>

    <!-- Current Promotions -->
    <section class="py-20" style="background-color: #0A0A0A;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Current Promotions</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p class="text-xl max-w-3xl mx-auto" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
            Take advantage of our exclusive deals and save on premium spirits, food, and services. 
            New promotions added regularly!
          </p>
        </div>

        <!-- Promotions Grid -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Coffee Promotion -->
          <div class="rounded-2xl shadow-2xl relative overflow-hidden" style="background-color: #1A1A1A;">
            <div class="absolute top-4 right-4 px-3 py-1 rounded-full text-sm font-bold" style="background-color: #D4AF37; color: #0A0A0A;">Save $0.10</div>
            <NuxtImg 
              src="/images/coffee-promo.jpg" 
              alt="Fresh Coffee Promotion"
              class="w-full h-48 object-cover opacity-80"
            />
            <div class="p-6">
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Fresh Coffee Special</h3>
              <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Get $0.10 off any large coffee. Available all day, every day!
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span style="color: #D4AF37;">December 31, 2024</span>
                </div>
                <div class="flex justify-between">
                  <span>Available</span>
                  <span style="color: #D4AF37;">All Day</span>
                </div>
                <div class="flex justify-between">
                  <span>Size</span>
                  <span style="color: #D4AF37;">Large Only</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Visit Store</button>
            </div>
          </div>

          <!-- Snacks Promotion -->
          <div class="rounded-2xl shadow-2xl relative overflow-hidden" style="background-color: #1A1A1A;">
            <div class="absolute top-4 right-4 px-3 py-1 rounded-full text-sm font-bold" style="background-color: #D4AF37; color: #0A0A0A;">Buy 2 Get 1</div>
            <NuxtImg 
              src="/images/snacks-promo.jpg" 
              alt="Snacks Promotion"
              class="w-full h-48 object-cover opacity-80"
            />
            <div class="p-6">
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Snack Attack Deal</h3>
              <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Buy 2 snacks, get 1 free! Mix and match any chips, candy, or crackers.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span style="color: #D4AF37;">January 15, 2025</span>
                </div>
                <div class="flex justify-between">
                  <span>Minimum</span>
                  <span style="color: #D4AF37;">2 Items</span>
                </div>
                <div class="flex justify-between">
                  <span>Exclusions</span>
                  <span style="color: #D4AF37;">Hot Food</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Visit Store</button>
            </div>
          </div>

          <!-- Car Wash Promotion -->
          <div class="rounded-2xl shadow-2xl relative overflow-hidden" style="background-color: #1A1A1A;">
            <div class="absolute top-4 right-4 px-3 py-1 rounded-full text-sm font-bold" style="background-color: #D4AF37; color: #0A0A0A;">$2 Off</div>
            <NuxtImg 
              src="/images/car-wash-promo.jpg" 
              alt="Car Wash Promotion"
              class="w-full h-48 object-cover opacity-80"
            />
            <div class="p-6">
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Car Wash Special</h3>
              <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                $2 off premium car wash. Valid through the end of this month.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span style="color: #D4AF37;">End of Month</span>
                </div>
                <div class="flex justify-between">
                  <span>Service</span>
                  <span style="color: #D4AF37;">Premium Wash</span>
                </div>
                <div class="flex justify-between">
                  <span>Savings</span>
                  <span style="color: #D4AF37;">$2.00</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Get Service</button>
            </div>
          </div>

          <!-- Fuel Promotion -->
          <div class="rounded-2xl shadow-2xl relative overflow-hidden" style="background-color: #1A1A1A;">
            <div class="absolute top-4 right-4 px-3 py-1 rounded-full text-sm font-bold" style="background-color: #D4AF37; color: #0A0A0A;">$0.05 Off</div>
            <NuxtImg 
              src="/images/fuel-promo.jpg" 
              alt="Fuel Promotion"
              class="w-full h-48 object-cover opacity-80"
            />
            <div class="p-6">
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Weekend Fuel Deal</h3>
              <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                $0.05 off per gallon on weekends. Fill up and save!
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Valid Days</span>
                  <span style="color: #D4AF37;">Saturday & Sunday</span>
                </div>
                <div class="flex justify-between">
                  <span>Minimum</span>
                  <span style="color: #D4AF37;">10 Gallons</span>
                </div>
                <div class="flex justify-between">
                  <span>Savings</span>
                  <span style="color: #D4AF37;">$0.05/gal</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Get Fuel</button>
            </div>
          </div>

          <!-- Hot Food Promotion -->
          <div class="rounded-2xl shadow-2xl relative overflow-hidden" style="background-color: #1A1A1A;">
            <div class="absolute top-4 right-4 px-3 py-1 rounded-full text-sm font-bold" style="background-color: #D4AF37; color: #0A0A0A;">Combo Deal</div>
            <NuxtImg 
              src="/images/hot-food-promo.jpg" 
              alt="Hot Food Promotion"
              class="w-full h-48 object-cover opacity-80"
            />
            <div class="p-6">
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Lunch Combo</h3>
              <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Sandwich + chips + drink for just $7.99. Perfect lunch deal!
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span style="color: #D4AF37;">February 28, 2025</span>
                </div>
                <div class="flex justify-between">
                  <span>Time</span>
                  <span style="color: #D4AF37;">11 AM - 2 PM</span>
                </div>
                <div class="flex justify-between">
                  <span>Price</span>
                  <span style="color: #D4AF37;">$7.99</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Order Now</button>
            </div>
          </div>

          <!-- Loyalty Program -->
          <div class="rounded-2xl shadow-2xl relative overflow-hidden" style="background-color: #1A1A1A;">
            <div class="absolute top-4 right-4 px-3 py-1 rounded-full text-sm font-bold" style="background-color: #D4AF37; color: #0A0A0A;">Join Free</div>
            <NuxtImg 
              src="/images/loyalty-promo.jpg" 
              alt="Loyalty Program"
              class="w-full h-48 object-cover opacity-80"
            />
            <div class="p-6">
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Loyalty Rewards</h3>
              <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Join our loyalty program and earn points on every purchase. Free to join!
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Sign Up</span>
                  <span style="color: #D4AF37;">Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Points</span>
                  <span style="color: #D4AF37;">1 per $1</span>
                </div>
                <div class="flex justify-between">
                  <span>Reward</span>
                  <span style="color: #D4AF37;">$5 off $50</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Join Now</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Promotion Terms -->
    <section class="py-20" style="background-color: #0F0F0F;">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Promotion Terms & Conditions</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
            Please read the terms and conditions for our current promotions.
          </p>
        </div>

        <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
          <div class="space-y-6">
            <div>
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">General Terms</h3>
              <ul class="text-sm space-y-1" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <li>• Promotions are subject to availability and may be discontinued without notice</li>
                <li>• Cannot be combined with other offers unless specified</li>
                <li>• Management reserves the right to modify or cancel promotions</li>
                <li>• Valid only at Go For It Liquor location</li>
              </ul>
            </div>

            <div>
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Fuel Promotions</h3>
              <ul class="text-sm space-y-1" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <li>• Fuel promotions apply to cash and credit purchases</li>
                <li>• Minimum purchase requirements may apply</li>
                <li>• Prices subject to change without notice</li>
                <li>• Promotion valid only during specified time periods</li>
              </ul>
            </div>

            <div>
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Food & Store Promotions</h3>
              <ul class="text-sm space-y-1" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <li>• While supplies last</li>
                <li>• Cannot be combined with other food promotions</li>
                <li>• Exclusions may apply to certain items</li>
                <li>• Valid only during store hours</li>
              </ul>
            </div>

            <div>
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Service Promotions</h3>
              <ul class="text-sm space-y-1" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <li>• Service promotions require appointment scheduling</li>
                <li>• Valid only during service hours</li>
                <li>• Additional fees may apply for premium services</li>
                <li>• Cannot be combined with other service discounts</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact for Promotions -->
    <section class="py-20" style="background-color: #D4AF37;">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-4xl font-bold mb-8" style="color: #0A0A0A; font-family: 'Playfair Display', serif;">Questions About Our Promotions?</h2>
        <p class="text-xl mb-8" style="color: #0A0A0A; font-family: 'Inter', sans-serif;">
          Contact us for more information about current promotions or to learn about upcoming deals.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a href="tel:+16513952174" class="py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #0A0A0A; color: #D4AF37; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#1A1A1A';" onmouseout="this.style.backgroundColor='#0A0A0A';">
            Call Now
          </a>
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="py-3 px-6 rounded-lg font-medium transition-all duration-300 border-2" style="border-color: #0A0A0A; color: #0A0A0A; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#0A0A0A'; this.style.color='#D4AF37';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#0A0A0A';">
            Visit Store
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Promotions & Deals — Go For It Liquor East Bethel, MN | Special Offers',
  meta: [
    { name: 'description', content: 'Current promotions and special offers at Go For It Liquor in East Bethel, MN. Save on premium spirits, food, car wash, and more. New deals added regularly!' },
    { name: 'keywords', content: 'promotions East Bethel MN, liquor store deals, discounts, fuel savings, coffee specials, car wash deals, Minnesota liquor store offers' },
    { name: 'canonical', content: 'https://go-for-it-wheat.vercel.app/promotions' }
  ],
  link: [
    { rel: 'sitemap', href: '/sitemap.xml', type: 'application/xml' }
  ]
})
</script>
