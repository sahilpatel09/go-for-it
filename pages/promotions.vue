<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/promotions-hero.jpg" 
          alt="Current promotions at Go For It Gas"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">Save More at Go For It Gas</h1>
        <p class="text-lg text-shadow">Current promotions and special offers</p>
      </div>
    </section>

    <!-- Current Promotions -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Current Promotions</h2>
          <p class="text-xl text-neutral-600 max-w-3xl mx-auto">
            Take advantage of our current deals and save money on fuel, food, and services. 
            New promotions added regularly!
          </p>
        </div>

        <!-- Promotions Grid -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Coffee Promotion -->
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Save $0.10</div>
            <NuxtImg 
              src="/images/coffee-promo.jpg" 
              alt="Fresh Coffee Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-3 mb-2">Fresh Coffee Special</h3>
              <p class="text-neutral-600 mb-4">
                Get $0.10 off any large coffee. Available all day, every day!
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span>December 31, 2024</span>
                </div>
                <div class="flex justify-between">
                  <span>Available</span>
                  <span>All Day</span>
                </div>
                <div class="flex justify-between">
                  <span>Size</span>
                  <span>Large Only</span>
                </div>
              </div>
              <button class="btn-primary w-full">Visit Store</button>
            </div>
          </div>

          <!-- Snacks Promotion -->
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Buy 2 Get 1</div>
            <NuxtImg 
              src="/images/snacks-promo.jpg" 
              alt="Snacks Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-3 mb-2">Snack Attack Deal</h3>
              <p class="text-neutral-600 mb-4">
                Buy 2 snacks, get 1 free! Mix and match any chips, candy, or crackers.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span>January 15, 2025</span>
                </div>
                <div class="flex justify-between">
                  <span>Minimum</span>
                  <span>2 Items</span>
                </div>
                <div class="flex justify-between">
                  <span>Exclusions</span>
                  <span>Hot Food</span>
                </div>
              </div>
              <button class="btn-primary w-full">Visit Store</button>
            </div>
          </div>

          <!-- Car Wash Promotion -->
          <div class="card relative overflow-hidden">
            <div class="promo-badge">$2 Off</div>
            <NuxtImg 
              src="/images/car-wash-promo.jpg" 
              alt="Car Wash Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-3 mb-2">Car Wash Special</h3>
              <p class="text-neutral-600 mb-4">
                $2 off premium car wash. Valid through the end of this month.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span>End of Month</span>
                </div>
                <div class="flex justify-between">
                  <span>Service</span>
                  <span>Premium Wash</span>
                </div>
                <div class="flex justify-between">
                  <span>Savings</span>
                  <span>$2.00</span>
                </div>
              </div>
              <button class="btn-primary w-full">Get Service</button>
            </div>
          </div>

          <!-- Fuel Promotion -->
          <div class="card relative overflow-hidden">
            <div class="promo-badge">$0.05 Off</div>
            <NuxtImg 
              src="/images/fuel-promo.jpg" 
              alt="Fuel Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-3 mb-2">Weekend Fuel Deal</h3>
              <p class="text-neutral-600 mb-4">
                $0.05 off per gallon on weekends. Fill up and save!
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Valid Days</span>
                  <span>Saturday & Sunday</span>
                </div>
                <div class="flex justify-between">
                  <span>Minimum</span>
                  <span>10 Gallons</span>
                </div>
                <div class="flex justify-between">
                  <span>Savings</span>
                  <span>$0.05/gal</span>
                </div>
              </div>
              <button class="btn-primary w-full">Get Fuel</button>
            </div>
          </div>

          <!-- Hot Food Promotion -->
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Combo Deal</div>
            <NuxtImg 
              src="/images/hot-food-promo.jpg" 
              alt="Hot Food Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-3 mb-2">Lunch Combo</h3>
              <p class="text-neutral-600 mb-4">
                Sandwich + chips + drink for just $7.99. Perfect lunch deal!
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Valid Until</span>
                  <span>February 28, 2025</span>
                </div>
                <div class="flex justify-between">
                  <span>Time</span>
                  <span>11 AM - 2 PM</span>
                </div>
                <div class="flex justify-between">
                  <span>Price</span>
                  <span>$7.99</span>
                </div>
              </div>
              <button class="btn-primary w-full">Order Now</button>
            </div>
          </div>

          <!-- Loyalty Program -->
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Join Free</div>
            <NuxtImg 
              src="/images/loyalty-promo.jpg" 
              alt="Loyalty Program"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-3 mb-2">Loyalty Rewards</h3>
              <p class="text-neutral-600 mb-4">
                Join our loyalty program and earn points on every purchase. Free to join!
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Sign Up</span>
                  <span>Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Points</span>
                  <span>1 per $1</span>
                </div>
                <div class="flex justify-between">
                  <span>Reward</span>
                  <span>$5 off $50</span>
                </div>
              </div>
              <button class="btn-primary w-full">Join Now</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Promotion Terms -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <h2 class="heading-2 mb-4">Promotion Terms & Conditions</h2>
          <p class="text-neutral-600">
            Please read the terms and conditions for our current promotions.
          </p>
        </div>

        <div class="bg-white rounded-xl p-8 shadow-soft">
          <div class="space-y-6">
            <div>
              <h3 class="heading-4 mb-2">General Terms</h3>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• Promotions are subject to availability and may be discontinued without notice</li>
                <li>• Cannot be combined with other offers unless specified</li>
                <li>• Management reserves the right to modify or cancel promotions</li>
                <li>• Valid only at Go For It Gas location</li>
              </ul>
            </div>

            <div>
              <h3 class="heading-4 mb-2">Fuel Promotions</h3>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• Fuel promotions apply to cash and credit purchases</li>
                <li>• Minimum purchase requirements may apply</li>
                <li>• Prices subject to change without notice</li>
                <li>• Promotion valid only during specified time periods</li>
              </ul>
            </div>

            <div>
              <h3 class="heading-4 mb-2">Food & Store Promotions</h3>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• While supplies last</li>
                <li>• Cannot be combined with other food promotions</li>
                <li>• Exclusions may apply to certain items</li>
                <li>• Valid only during store hours</li>
              </ul>
            </div>

            <div>
              <h3 class="heading-4 mb-2">Service Promotions</h3>
              <ul class="text-sm text-neutral-600 space-y-1">
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
    <section class="py-16 bg-primary-500">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
        <h2 class="heading-2 mb-8">Questions About Our Promotions?</h2>
        <p class="text-xl mb-8">
          Contact us for more information about current promotions or to learn about upcoming deals.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a href="tel:+16513952174" class="btn-secondary">
            Call Now
          </a>
          <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-outline border-white text-white hover:bg-white hover:text-primary-500">
            Visit Store
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Promotions - Go For It Gas',
  meta: [
    { name: 'description', content: 'Current promotions and special offers at Go For It Gas. Save on fuel, food, car wash, and more. New deals added regularly!' },
    { name: 'keywords', content: 'promotions, deals, discounts, fuel savings, coffee specials, car wash deals, East Bethel' }
  ]
})
</script>
