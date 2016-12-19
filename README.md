# aiocall
The missing call methods for [python asyncio](http://docs.python.org/3/library/asyncio).

I found that python asyncio is lacking some basic methods to invoke calls:
```python3
call_soon_periodic(interval, callback, *args)
call_later_periodic(delay, interval, callback, *args)
```

This lib provides these methods.

Example:
```python3
loop = asyncio.get_event_loop()

def do_something(what):
    print('doing %s...' % what)

timer1 = call_soon_periodic(1.0, do_something, 'stuff')
timer2 = call_later_periodic(0.5, 1.0, do_something, 'other stuff')

loop.call_later(2.7, timer1.cancel)
loop.call_later(2.8, timer2.cancel)

loop.call_later(2.9, loop.stop)

print('starting loop')
loop.run_forever()
print('loop done')

loop.close()
```

Produces:
```
starting loop
doing stuff...
doing other stuff...
doing stuff...
doing other stuff...
doing stuff...
doing other stuff...
loop done
```
