<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-80 flex items-center justify-center overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-amber-900">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/jack_daniel.png" 
          alt="Premium Liquor Selection at Go For It Liquor"
          class="w-full h-full object-cover opacity-20"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-slate-900/80 via-slate-800/70 to-amber-900/80"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="text-4xl md:text-6xl font-bold mb-6 text-shadow-lg">Premium Liquor Selection</h1>
        <p class="text-xl md:text-2xl text-amber-100 text-shadow">Quality spirits, beer, and wine for every occasion</p>
      </div>
    </section>

    <!-- Liquor Showcase -->
    <section class="py-20 bg-slate-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-white mb-6">Our Liquor Collection</h2>
          <p class="text-xl text-slate-300">From premium spirits to craft beers and fine wines</p>
        </div>

        <!-- Premium Spirits Showcase -->
        <div class="mb-16">
          <div class="text-center mb-8">
            <h3 class="text-3xl font-bold text-white mb-4">Premium Spirits Collection</h3>
            <p class="text-lg text-slate-300 max-w-3xl mx-auto">
              Discover our carefully curated selection of premium spirits, featuring iconic brands and exceptional quality.
            </p>
          </div>
          
          <!-- Featured Jack Daniel's Collection -->
          <div class="bg-gradient-to-r from-amber-800 to-amber-700 rounded-2xl p-8 mb-12 shadow-2xl">
            <div class="text-center mb-8">
              <h4 class="text-2xl font-bold text-white mb-2">Jack Daniel's Collection</h4>
              <p class="text-amber-100">Tennessee's finest whiskey, crafted with tradition and excellence</p>
            </div>
            
            <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
              <div class="bg-slate-800 rounded-lg p-6 shadow-lg hover:bg-slate-700 transition-colors duration-300">
                <div class="flex items-center space-x-6">
                  <NuxtImg 
                    src="/jack_daniel.png" 
                    alt="Jack Daniel's Old No. 7"
                    class="w-20 h-28 object-contain"
                  />
                  <div class="flex-1">
                    <h5 class="font-bold text-lg mb-2 text-white">Jack Daniel's Old No. 7</h5>
                    <p class="text-sm text-slate-300 mb-3">The original Tennessee whiskey with a smooth, mellow taste</p>
                    <div class="flex items-center justify-between">
                      <span class="text-2xl font-bold text-amber-400">$24.99</span>
                      <span class="text-sm text-slate-400">750ml</span>
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="bg-slate-800 rounded-lg p-6 shadow-lg hover:bg-slate-700 transition-colors duration-300">
                <div class="flex items-center space-x-6">
                  <NuxtImg 
                    src="/jack.jpg" 
                    alt="Jack Daniel's Gentleman Jack"
                    class="w-20 h-28 object-contain"
                  />
                  <div class="flex-1">
                    <h5 class="font-bold text-lg mb-2 text-white">Jack Daniel's Gentleman Jack</h5>
                    <p class="text-sm text-slate-300 mb-3">Double-mellowed for exceptional smoothness and character</p>
                    <div class="flex items-center justify-between">
                      <span class="text-2xl font-bold text-amber-400">$32.99</span>
                      <span class="text-sm text-slate-400">750ml</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Featured Products -->
        <div class="mb-16">
          <h3 class="text-3xl font-bold text-white mb-8 text-center">More Premium Spirits</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <!-- Crown Royal -->
            <div class="bg-slate-700 rounded-lg p-4 text-center hover:bg-slate-600 transition-colors duration-300">
              <NuxtImg 
                src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                alt="Crown Royal Canadian Whisky"
                class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
              />
              <h4 class="font-semibold text-sm mb-1 text-white">Crown Royal</h4>
              <p class="text-xs text-slate-300 mb-2">Canadian Whisky</p>
              <p class="text-sm font-semibold text-amber-400">$26.99</p>
            </div>

            <!-- Tito's Vodka -->
            <div class="bg-slate-700 rounded-lg p-4 text-center hover:bg-slate-600 transition-colors duration-300">
              <NuxtImg 
                src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
                alt="Tito's Handmade Vodka"
                class="w-24 h-32 object-cover rounded-lg mx-auto mb-4"
              />
              <h4 class="font-semibold text-sm mb-1 text-white">Tito's Handmade</h4>
              <p class="text-xs text-slate-300 mb-2">Vodka</p>
              <p class="text-sm font-semibold text-amber-400">$22.99</p>
            </div>

            <!-- Captain Morgan -->
            <div class="card">
              <div class="card-body text-center">
                <NuxtImg 
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
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
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
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
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
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
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
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
                  src="https://images.unsplash.com/photo-1608270586620-248524c67de9?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" 
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
          <h3 class="text-3xl font-bold text-white mb-8 text-center">Beer Selection</h3>
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
          <h3 class="text-3xl font-bold text-white mb-8 text-center">Wine Selection</h3>
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
        <div class="bg-gradient-to-r from-slate-700 to-slate-600 rounded-2xl p-8 mb-16">
          <div class="text-center mb-8">
            <h3 class="text-3xl font-bold text-white mb-4">Why Choose Go For It Liquor?</h3>
            <p class="text-lg text-slate-300">We're more than just a gas station - we're your premium liquor destination</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="text-center">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2 text-white">Curated Selection</h4>
              <p class="text-sm text-slate-300">Hand-picked premium brands</p>
            </div>

            <div class="text-center">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2 text-white">Convenient Hours</h4>
              <p class="text-sm text-slate-300">Open daily 6 AM - 10 PM</p>
            </div>

            <div class="text-center">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2 text-white">Competitive Prices</h4>
              <p class="text-sm text-slate-300">Great value on premium spirits</p>
            </div>

            <div class="text-center">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2 text-white">Local Convenience</h4>
              <p class="text-sm text-slate-300">Right here in East Bethel</p>
            </div>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="text-center">
          <h3 class="text-3xl font-bold text-white mb-4">Ready to Explore Our Selection?</h3>
          <p class="text-xl text-slate-300 mb-8">Visit us today and discover your new favorite spirit</p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="bg-amber-600 hover:bg-amber-700 text-white px-8 py-4 text-lg font-semibold rounded-lg shadow-lg hover:shadow-xl transition-all duration-300">
              Get Directions
            </a>
            <a href="tel:+16513952174" class="bg-transparent border-2 border-amber-400 text-amber-400 hover:bg-amber-400 hover:text-slate-900 px-8 py-4 text-lg font-semibold rounded-lg transition-all duration-300">
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
  title: 'Premium Liquor Selection - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Discover our premium liquor selection at Go For It Liquor. Quality spirits, craft beer, and fine wines. Conveniently located in East Bethel, MN.' },
    { name: 'keywords', content: 'liquor, spirits, whiskey, vodka, rum, tequila, craft beer, wine, premium alcohol, East Bethel, Jack Daniels' }
  ]
})
</script>
