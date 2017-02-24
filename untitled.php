
<?php if(!is_page_template('template-specializedlogin.php')){ get_header();} else{ get_header('login');} ?>

<?php if(!is_page_template('template-specializedlogin.php')) { ?>
	<!--secondary menu-->
		<div class="row" style="padding-top:0px;">
			<div class="twelve columns" id="menu_container" >

		<?php $navcheck = '' ; ?>

	<?php $navcheck = wp_nav_menu( array( 'container_class' => 'menu-header2', 'theme_location' => 'secondary' , 'menu_id' => 'nav', 'fallback_cb' => '', 'echo' => false ) ); ?>

 <?php  if ($navcheck == '') { ?>

	<ul id="nav">
		<?php wp_list_pages('title_li=&sort_column=menu_order'); ?>

	</ul>
<?php } else echo($navcheck); ?>

	</div>
</div>

<?php } ?>





<!-- slider -->
<?php if(is_front_page()) { ?>
<div class = "row" style="padding-top:5px;">
<!-- <hr style="margin:0px; height: 3px; color: #bf9900;background-color: #bf9900; border:none;"> -->

<b style="font-size:20px; color:#bf9900; background-color:#FFF; padding-top:10px; width:100%; display:block; text-align:center;
">Transforming Math Education Through Computing</b>

<!--
<a target="_blank" href="http://c-stem.ucdavis.edu/scoreboard/all_scores/4"><b style="font-size:20px; color:#bf9900; background-color:#FFF; padding-top:10px; width:100%; display:block; text-align:center;
">C-STEM Day Scoreboard</b></a>
-->

<!--
<b style="font-size:20px; color:#bf9900; background-color:#FFF; padding-top:10px; width:100%; display:block; text-align:center;
">Transforming Math Education through Computing</b>-->
</div>
<div id="slider_container">

	<div class="row">

		<div class="four columns">
		<?php

	if (  dynamic_sidebar( 'first-footer-widget-area' ) ) : ?>


		<?php endif; // end primary widget area ?>



		</div>

		<div class="eight columns">
			<?php get_template_part( 'element-slider', 'index' ); ?>
		</div>

	</div>
</div>

<?php } ?> <!-- slider end -->


<!-- home boxes -->
<?php if(is_front_page()) { ?>

	<div class="row" id="box_container">

		<?php get_template_part( 'element-boxes', 'index' ); ?>

	</div>

<!-- home boxes end -->

<?php if(is_front_page()) { ?>
</div>
<div id="slider_container">

	<div class="row">

		<div class="eight columns">
			<li>
			 	<a href="https://www.youtube.com/watch?v=4CCYA-_jQbs&feature=youtu.be"><img src="http://c-stem.ucdavis.edu/wp-content/uploads/2013/07/Screen-Shot-2016-07-15-at-2.56.33-PM.png" alt="Make_Math_Fun_with_Robotics" /></a>
				<p class="flex-caption" style="font-weight:bold;">Make Math Fun with Robotics<p>
			</li>
		</div>

		<div class="four columns">
			<a class="twitter-timeline"
  				href="https://twitter.com/ucdcstem"
  				data-width="300"
  				data-height="300">
				Tweets by @UCD CSTEM
			</a>
		</div>

	</div>
</div>

<?php } ?> 

<div class="clear"></div>
<div class="row" style="height:65px; margin-top: 15px";>
<div style="float:left; height: 65px; text-align: left; margin-left: 25px;">
	<span style=" font-size: 12px; color: #002666; font-weight: bold; ">Major Sponsors:</span>
	<a target="_blank" style="margin-left: 10px" href="http://www.nsf.gov"><img style="max-height: 65px; vertical-align: middle" height="65px" src="http://c-stem.ucdavis.edu/wp-content/uploads/logo/nsf-150x150.png" /></a>
	<a target="_blank" style="margin-left: 10px" href="http://www.cde.ca.gov/"><img style="max-height: 65px; vertical-align: middle" height="65x" src="http://c-stem.ucdavis.edu/wp-content/uploads/logo/cde_244x75.png"></a>
</div>





<div class="one columns" style="margin-top: 20px; width: 175px; height: 50px; text-align: left; margin-left: 5px; float: right; margin-right: 100px; ">
	<!--<?php echo knews_plugin_form(array(1,  'stylize'=>1, 'labelwhere'=>'outside', 'subtitle'=>0, 'requiredtext'=>0, 'terms'=>0, 'script'=>1)); ?>-->
<?php echo knews_plugin_form(); ?>
</div></div>

<?php } ?>
<!--content-->
<?php if(!is_front_page()){?>
		<div class="row" id="content_container">
<?php get_sidebar(); ?>

	<!--left col--><div class="ten columns">

		<div id="left-col">

			<?php get_template_part( 'loop', 'index' ); ?>

	</div> <!--left-col end-->
</div> <!--column end-->

</div>
<!--content end-->
<?php } ?>
<?php get_footer(); ?>