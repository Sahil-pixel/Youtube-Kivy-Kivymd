package org.test.kivmob_test;

import android.util.Log;
import androidx.annotation.NonNull;
import com.google.android.gms.ads.LoadAdError;
import com.google.android.gms.ads.rewarded.RewardedAd;
import com.google.android.gms.ads.rewarded.RewardedAdLoadCallback;
import com.google.android.gms.ads.FullScreenContentCallback;
import com.google.android.gms.ads.AdError;

public class RewardedAdLoadCallback4kivy extends RewardedAdLoadCallback {

    private static final String TAG = "RewardedAdLoadCallback4kivy";
    private RewardedAd mRewardedAd;

    @Override
    public void onAdLoaded(@NonNull RewardedAd rewardedAd) {
        // What to do if an ad loads successfully is here
        // ie. perform ad display and playback
        mRewardedAd = rewardedAd;
        Log.d(TAG, "Rewarded Ad was loaded.");
        mRewardedAd.setFullScreenContentCallback(new FullScreenContentCallback() {
            @Override
            public void onAdClicked() {
              // Called when a click is recorded for an ad.
              Log.d(TAG, "Rewarded Ad was clicked.");
            }

             @Override
            public void onAdDismissedFullScreenContent() {
              // Called when ad is dismissed.
              // Set the ad reference to null so you don't show the ad a second time.
              Log.d(TAG, "Rewarded Ad dismissed fullscreen content.");
              mRewardedAd = null;
            }

            @Override
            public void onAdFailedToShowFullScreenContent(AdError adError) {
              // Called when ad fails to show.
              Log.e(TAG, "Rewarded Ad failed to show fullscreen content.");
              mRewardedAd = null;
            }

            @Override
            public void onAdImpression() {
              // Called when an impression is recorded for an ad.
              Log.d(TAG, "Rewarded Ad recorded an impression.");
            }

            @Override
            public void onAdShowedFullScreenContent() {
              // Called when ad is shown.
              Log.d(TAG, "Rewarded Ad showed fullscreen content.");
            }
          });
    }

    @Override
    public void onAdFailedToLoad(@NonNull LoadAdError loadAdError) {
        // What to do if the ad fails to load is here
        // ie. obtain the cause of the error and detailed information
        Log.d(TAG, loadAdError.toString());
        mRewardedAd = null;
    }
}
