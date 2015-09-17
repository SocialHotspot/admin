if(client_slug) {
	(function(window, document, $, client_slug) {

		var commands = {
			'create-unifi-site': function(cb) {
				$.post('/unifi/create-site/',
					   { 
						   
						 unifi_site_id: $('#unifi_site_id').val(),
						 unifi_site_name: $('#unifi_site_name').val(),
						 unifi_controller: 1
						 
					   }, cb);
			},
				
			'set-general-settings': function(cb) {
				$.post('/unifi/set-general-settings/',
					   { 
						   
						 unifi_site_id: $('#unifi_site_id').val(),
						 unifi_controller: 1
						 
					   }, cb);
			},
			
			'set-guest-portal-settings': function(cb) {
				$.post('/unifi/set-guest-portal/',
					   { 
						   
						 unifi_site_id: $('#unifi_site_id').val(),
						 unifi_controller: 1
						 
					   }, cb);
			},
			
			'add-wireless-networks': function(cb) {
				$.post('/unifi/add-wlans/',
					   { 
						   
						 unifi_site_id: $('#unifi_site_id').val(),
						 unifi_controller: 1,
						 
						 ssid: $('#ssid').val(),
						 ssid_private: $('#ssid_private').val(),
						 password_private: $('#password_private').val(),
						 
					   }, cb);
			},
			
			'attach-access-points': function(cb) {
				$.post('/clients/detail/'+ client_slug +'/add-hotspots/',
					   { 
						   
						 number_of_aps: $('#number_of_aps').val()
						 
					   }, function(data) {
						   if(data.hotspots) {
							   data.hotspots.forEach(function(hotspot) {
								  var line = $('<li><div class="ui-grid-a"><div class="ui-block-a"></div><div class="ui-block-b"></div></div></li>');
								  
								  line.find('.ui-block-a').text(hotspot.mac_address);
								  line.find('.ui-block-b').text(hotspot.external_id);
								   
								  $('#aps').append(line);
							   });
							   
							   $('#aps').prepend($('<li data-role="list-divider"></li>').text('Attached access points'));
							   
							   $('#aps').listview('refresh');
							   
							   $('#aps_container').slideDown();
							   
							   cb();
						   } else {
						   	   cb(false);
						   }
					   }, 'json');
			}
		};
		
		var running_all = false;
		
		var transitionButton = function(button, cb) {
			var originalText = $(button).text();
			
			$(button).text($(button).parent('.step').attr('data-busy-text'));
				     
			$(button).animate({ 'opacity': '0.85' }, 250);
			
			step_id = $(button).parent('.step').attr('id')
			
			commands[step_id](function(success) {
				if(success != false) {
					$(button).text($(button).parent('.step').attr('data-done-text'))
						 .buttonMarkup({ icon: 'check' });
				} else {
					$(button).text('Something went wrong.')
						 .buttonMarkup({ icon: 'alert' });
				}
			
				$(button).parents('.ui-listview')
				         .animate({ 'opacity': '0.4' }, 250);
				
				cb($(button).parent('.step'));
			});
		}
		
		var nextStep = function(step) {
			$('#'+ step.attr('data-next-step')).parents('.ui-listview')
										       .animate({ 'opacity': '1.0' }, 250);
			
			if(running_all) {
	
				if(step.attr('data-next-step')) {
					$('#'+ step.attr('data-next-step') +' .submit-button').click();
					
					$('body').animate({ scrollTop: step.offset().top - $('body').offset().top + $('body').scrollTop() }, '250', 'swing');
				} else {
					
					$('body').animate({ scrollTop: $('#finish').offset().top - $('body').offset().top + $('body').scrollTop() }, '250', 'swing');
					
					$('#finish').animate({ 'opacity': '1.0' }, 200);
					
				}
				
			}
		}
		
		$(document).ready(function() {
			$('#run-all').click(function() {
				var clicked = this;
				running_all = true;
				
				$('.submit-button')[1].click();
				
			});
			
			$('.submit-button').click(function() {
				if($(this).attr('id') != 'run-all') {
					transitionButton(this, nextStep);
				}
			});
			
			$('#finish button').click(function() {
				$.post('/clients/detail/'+ client_slug +'/set-unifi-site/',
				   { 
					   
					 unifi_site_id: $('#unifi_site_id').val(),
					 unifi_controller: 1
					 
				   }, function(data) {
					   
					   window.location.reload();
					   
				   });
			});
			
		});
	
	})(window, document, window.jQuery, client_slug);
}