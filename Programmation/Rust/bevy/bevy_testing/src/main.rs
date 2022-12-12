use bevy::prelude::*;

#[derive(Component)]
struct Health {
    hp: f32, 
    extra: f32,
}

#[derive(Component)]
struct PlayerXp(u32);

#[derive(Component)]
struct PlayerName(String);


/// "You can use empty structs to help you identify specific entities. These are known as "marker components"""

///Add this to all menu ui entities to help identify them
#[derive(Component)]
struct MainMenuUI;

/// Marker for hostile game units
#[derive(Component)]
struct Enemy;

/// This will be used to identify the main player entity
#[derive(Component)]
struct Player;

///Tag all creatures that are currently friendly towards the player
#[derive(Component)]
struct Friendly;

#[derive(Bundle)]
struct PlayerBundle {
    xp : PlayerXp,
    name : PlayerName,
    health : Health,
    _p : Player,

    // We can nest/include another bundle.
    // Add the compoenents for a standard Bevy Sprite: 
    //#[bundle]
    //sprite : SpriteSheetBundle,
}


fn main(){
    App::new()
        .add_plugins(DefaultPlugins)
        .run();
}