package org.test.kivmob_test;

import android.util.Log;
import androidx.annotation.NonNull;
import com.google.android.gms.ads.LoadAdError;
import com.google.android.gms.ads.interstitial.InterstitialAd;
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback;
import com.google.android.gms.ads.FullScreenContentCallback;
import com.google.android.gms.ads.AdError;



public class InterstitialAdLoadCallback4kivy extends InterstitialAdLoadCallback {

    private static final String TAG = "InterstitialAdLoadCallback4kivy";
    private InterstitialAd mInterstitialAd;

    @Override
    public void onAdLoaded(@NonNull InterstitialAd interstitialAd) {
        // What to do if an ad loads successfully is here :
        mInterstitialAd = interstitialAd;
        Log.d(TAG, "Interstitial Ad loaded.");

        // Process for a loaded ad is here
        mInterstitialAd.setFullScreenContentCallback(new FullScreenContentCallback(){
            @Override
            public void onAdClicked() {
              // Called when a click is recorded for an ad.
              Log.d(TAG, "Interstitial Ad was clicked.");
            }

            @Override
            public void onAdDismissedFullScreenContent() {
              // Called when ad is dismissed.
              // Set the ad reference to null so you don't show the ad a second time.
              Log.d(TAG, "Interstitial Ad dismissed fullscreen content.");
              mInterstitialAd = null;
            }

            @Override
            public void onAdFailedToShowFullScreenContent(AdError adError) {
              // Called when ad fails to show.
              Log.e(TAG, "Interstitial Ad failed to show fullscreen content.");
              mInterstitialAd = null;
            }

            @Override
            public void onAdImpression() {
              // Called when an impression is recorded for an ad.
              Log.d(TAG, "Interstitial Ad recorded an impression.");
            }

            @Override
            public void onAdShowedFullScreenContent() {
              // Called when ad is shown.
              Log.d(TAG, "Interstitial Ad showed fullscreen content.");
            }
          });
    }

    @Override
    public void onAdFailedToLoad(@NonNull LoadAdError loadAdError) {
        // What to do if the ad fails to load is here
        Log.d(TAG, "Failed to load Interstitial ad: " + loadAdError.getMessage());
        // Error handling and alternative processing in case of loading failure are here
        mInterstitialAd = null;
    }
}
