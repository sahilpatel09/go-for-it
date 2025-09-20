<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/img.webp" 
          alt="Go For It Gas Station - 3255 Viking Blvd NE, East Bethel, MN"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg text-white">Premium Liquor Selection</h1>
        <p class="text-lg text-shadow">Quality spirits, beer, and wine for every occasion</p>
      </div>
    </section>

    <!-- Liquor Showcase -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Our Liquor Collection</h2>
          <p class="text-xl text-neutral-600">From premium spirits to craft beers and fine wines</p>
        </div>

        <!-- Featured Products -->
        <div class="mb-16">
          <h3 class="heading-3 mb-8 text-center">Featured Products</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <!-- Jack Daniel's -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1569529465841-dfecdab7503b?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Jack Daniel's Tennessee Whiskey"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Jack Daniel's</h4>
                <p class="text-xs text-neutral-600 mb-2">Tennessee Whiskey</p>
                <p class="text-sm font-semibold text-primary-600">$24.99</p>
              </div>
            </div>

            <!-- Crown Royal -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1551538827-9c037cb4f32a?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Crown Royal Canadian Whisky"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Crown Royal</h4>
                <p class="text-xs text-neutral-600 mb-2">Canadian Whisky</p>
                <p class="text-sm font-semibold text-primary-600">$26.99</p>
              </div>
            </div>

            <!-- Tito's Vodka -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1544145945-f90425340c7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Tito's Handmade Vodka"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Tito's Handmade</h4>
                <p class="text-xs text-neutral-600 mb-2">Vodka</p>
                <p class="text-sm font-semibold text-primary-600">$22.99</p>
              </div>
            </div>

            <!-- Captain Morgan -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1570197788417-0e82375c9371?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Captain Morgan Spiced Rum"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Captain Morgan</h4>
                <p class="text-xs text-neutral-600 mb-2">Spiced Rum</p>
                <p class="text-sm font-semibold text-primary-600">$19.99</p>
              </div>
            </div>

            <!-- Patrón Tequila -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1551538827-9c037cb4f32a?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Patrón Silver Tequila"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Patrón Silver</h4>
                <p class="text-xs text-neutral-600 mb-2">Tequila</p>
                <p class="text-sm font-semibold text-primary-600">$49.99</p>
              </div>
            </div>

            <!-- Bacardi -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1570197788417-0e82375c9371?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Bacardi Superior White Rum"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Bacardi Superior</h4>
                <p class="text-xs text-neutral-600 mb-2">White Rum</p>
                <p class="text-sm font-semibold text-primary-600">$18.99</p>
              </div>
            </div>

            <!-- Fireball -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1569529465841-dfecdab7503b?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Fireball Cinnamon Whisky"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Fireball</h4>
                <p class="text-xs text-neutral-600 mb-2">Cinnamon Whisky</p>
                <p class="text-sm font-semibold text-primary-600">$16.99</p>
              </div>
            </div>

            <!-- Smirnoff -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1544145945-f90425340c7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Smirnoff Vodka"
                  class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Smirnoff</h4>
                <p class="text-xs text-neutral-600 mb-2">Vodka</p>
                <p class="text-sm font-semibold text-primary-600">$15.99</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Beer Selection -->
        <div class="mb-16">
          <h3 class="heading-3 mb-8 text-center">Beer Selection</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <!-- Budweiser -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Budweiser American Lager"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Budweiser</h4>
                <p class="text-xs text-neutral-600 mb-2">American Lager</p>
                <p class="text-sm font-semibold text-primary-600">$8.99</p>
              </div>
            </div>

            <!-- Coors Light -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Coors Light Lager"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Coors Light</h4>
                <p class="text-xs text-neutral-600 mb-2">Light Lager</p>
                <p class="text-sm font-semibold text-primary-600">$8.99</p>
              </div>
            </div>

            <!-- Miller Lite -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Miller Lite Lager"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Miller Lite</h4>
                <p class="text-xs text-neutral-600 mb-2">Light Lager</p>
                <p class="text-sm font-semibold text-primary-600">$8.99</p>
              </div>
            </div>

            <!-- Corona -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Corona Extra Mexican Lager"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Corona Extra</h4>
                <p class="text-xs text-neutral-600 mb-2">Mexican Lager</p>
                <p class="text-sm font-semibold text-primary-600">$9.99</p>
              </div>
            </div>

            <!-- Heineken -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Heineken Dutch Lager"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Heineken</h4>
                <p class="text-xs text-neutral-600 mb-2">Dutch Lager</p>
                <p class="text-sm font-semibold text-primary-600">$9.99</p>
              </div>
            </div>

            <!-- Stella Artois -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Stella Artois Belgian Lager"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Stella Artois</h4>
                <p class="text-xs text-neutral-600 mb-2">Belgian Lager</p>
                <p class="text-sm font-semibold text-primary-600">$10.99</p>
              </div>
            </div>

            <!-- Michelob Ultra -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Michelob Ultra Light Beer"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Michelob Ultra</h4>
                <p class="text-xs text-neutral-600 mb-2">Light Beer</p>
                <p class="text-sm font-semibold text-primary-600">$8.99</p>
              </div>
            </div>

            <!-- Guinness -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Guinness Irish Stout"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Guinness</h4>
                <p class="text-xs text-neutral-600 mb-2">Irish Stout</p>
                <p class="text-sm font-semibold text-primary-600">$9.99</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Wine Selection -->
        <div class="mb-16">
          <h3 class="heading-3 mb-8 text-center">Wine Selection</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <!-- Barefoot -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Barefoot Red Wine"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Barefoot</h4>
                <p class="text-xs text-neutral-600 mb-2">Red Wine</p>
                <p class="text-sm font-semibold text-primary-600">$6.99</p>
              </div>
            </div>

            <!-- Yellow Tail -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Yellow Tail Chardonnay"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Yellow Tail</h4>
                <p class="text-xs text-neutral-600 mb-2">Chardonnay</p>
                <p class="text-sm font-semibold text-primary-600">$7.99</p>
              </div>
            </div>

            <!-- Sutter Home -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Sutter Home White Zinfandel"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Sutter Home</h4>
                <p class="text-xs text-neutral-600 mb-2">White Zinfandel</p>
                <p class="text-sm font-semibold text-primary-600">$5.99</p>
              </div>
            </div>

            <!-- Franzia -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Franzia Box Wine"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Franzia</h4>
                <p class="text-xs text-neutral-600 mb-2">Box Wine</p>
                <p class="text-sm font-semibold text-primary-600">$12.99</p>
              </div>
            </div>

            <!-- Cupcake -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Cupcake Moscato"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Cupcake</h4>
                <p class="text-xs text-neutral-600 mb-2">Moscato</p>
                <p class="text-sm font-semibold text-primary-600">$8.99</p>
              </div>
            </div>

            <!-- Woodbridge -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Woodbridge Cabernet"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Woodbridge</h4>
                <p class="text-xs text-neutral-600 mb-2">Cabernet</p>
                <p class="text-sm font-semibold text-primary-600">$9.99</p>
              </div>
            </div>

            <!-- Kendall Jackson -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Kendall Jackson Chardonnay"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Kendall Jackson</h4>
                <p class="text-xs text-neutral-600 mb-2">Chardonnay</p>
                <p class="text-sm font-semibold text-primary-600">$12.99</p>
              </div>
            </div>

            <!-- Prosecco -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                  alt="Prosecco Sparkling Wine"
                  class="w-20 h-24 object-cover rounded-lg mx-auto mb-4"
                />
                <h4 class="font-semibold text-sm mb-1">Prosecco</h4>
                <p class="text-xs text-neutral-600 mb-2">Sparkling Wine</p>
                <p class="text-sm font-semibold text-primary-600">$11.99</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Special Features -->
        <div class="bg-gradient-to-r from-primary-50 to-accent-50 rounded-2xl p-8 mb-16">
          <div class="text-center mb-8">
            <h3 class="heading-3 mb-4">Why Choose Go For It Gas Liquor?</h3>
            <p class="text-lg text-neutral-600">We're more than just a gas station - we're your premium liquor destination</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Curated Selection</h4>
              <p class="text-sm text-neutral-600">Hand-picked premium brands</p>
            </div>

            <div class="text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Convenient Hours</h4>
              <p class="text-sm text-neutral-600">Open daily 6 AM - 10 PM</p>
            </div>

            <div class="text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Competitive Prices</h4>
              <p class="text-sm text-neutral-600">Great value on premium spirits</p>
            </div>

            <div class="text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Local Convenience</h4>
              <p class="text-sm text-neutral-600">Right here in East Bethel</p>
            </div>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="text-center">
          <h3 class="heading-3 mb-4">Ready to Explore Our Selection?</h3>
          <p class="text-xl text-neutral-600 mb-8">Visit us today and discover your new favorite spirit</p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-primary">
              Get Directions
            </a>
            <a href="tel:+16513952174" class="btn-secondary">
              Call Now
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// SEO Meta
useHead({
  title: 'Premium Liquor Selection - Go For It Gas',
  meta: [
    { name: 'description', content: 'Discover our premium liquor selection at Go For It Gas. Quality spirits, craft beer, and fine wines. Conveniently located in East Bethel, MN.' },
    { name: 'keywords', content: 'liquor, spirits, whiskey, vodka, rum, tequila, craft beer, wine, premium alcohol, East Bethel' }
  ]
})
</script>
