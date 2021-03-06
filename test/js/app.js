QUnit.test( "app new version available action", function( assert ) {

  var info = {};
  info.installed_version = 1.0;
  info.current_version = 1.1;

  assert.deepEqual( get_actions(info), ['open', 'upgrade', 'remove', 'check']);
});

QUnit.test( "app latest version action", function( assert ) {

  var info = {};
  info.installed_version = 1.1;
  info.current_version = 1.1;

  assert.deepEqual( get_actions(info) , ['open', 'remove', 'check'] );
});

QUnit.test( "app not installed action", function( assert ) {

  var info = {};
  info.current_version = 1.1;

  assert.deepEqual( get_actions(info), ['install', 'check']);
});